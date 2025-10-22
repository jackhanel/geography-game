from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from datetime import datetime
import time
from .models import User, dailyScores, dailyChallenges
from .data import getCountries, generateGameCategories, getCountryData
from . import db

views = Blueprint("views", __name__)

@views.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        if not current_user.is_authenticated:
            flash("You must be logged in to play the daily challenge.", category="error")
            return redirect(url_for("auth.login"))
        
        today = datetime.now().date()
        current_user_daily_challenge = dailyScores.query.filter_by(user_id=current_user.id, date=today).first()
        if not current_user_daily_challenge:
            return redirect(url_for("views.dailyChallenge"))
        else:
            flash("You have already reached your maximum attempts on today's daily challenge. Come back tomorrow for more!", category="warning")
    return render_template("home.html")


@views.route("/daily-challenge", methods=["POST", "GET"])
def dailyChallenge():

    # check if a daily challenge dataset already exists for today's date, and if not, fetch the data
    today = datetime.now().date()
    existing_daily_challenge = dailyChallenges.query.filter_by(date=today).first()
    if not existing_daily_challenge:
        countries = getCountries()
        game_category_information = generateGameCategories()
        game_category_backend_names = game_category_information[0]
        game_category_front_end_names = game_category_information[1]
        all_game_data = getCountryData(game_category_backend_names)

        # prepare the country ranks for the front end
        all_game_data_for_front_end = []
        for game_data in all_game_data:
            game_data_entry = {"game_category_backend_name": game_data["game_category_backend_name"], "game_category_front_end_name": game_data["game_category_front_end_name"]}
            country_ranks = []
            for country_rank in game_data["country_ranks"]:
                for country in countries:
                    if country_rank["country"] == country["country_name"]:
                        country_entry = {"country_name": country["country_name"], "flag": country["flag"], "rank": country_rank["rank"]}
                        country_ranks.append(country_entry)
            game_data_entry["country_ranks"] = country_ranks
            all_game_data_for_front_end.append(game_data_entry)

        # add today's daily challenge to the database
        new_daily_challenge = dailyChallenges(
            date = today,
            all_game_data_for_front_end=all_game_data_for_front_end,
            countries = countries,
            game_category_backend_names = game_category_backend_names,
            game_category_front_end_names = game_category_front_end_names
        )
        db.session.add(new_daily_challenge)
        db.session.commit()
    else:
        all_game_data_for_front_end = existing_daily_challenge.all_game_data_for_front_end
        countries = existing_daily_challenge.countries
        game_category_backend_names = existing_daily_challenge.game_category_backend_names
        game_category_front_end_names = existing_daily_challenge.game_category_front_end_names

    print(all_game_data_for_front_end)
    # when the user submits their game, add the date and score to the database
    if request.method == "POST":
        time.sleep(2)
        score = int(request.form.get("score", 0))
        new_daily_score = dailyScores(
            user_id = current_user.id,
            date = today,
            score = score
        )
        db.session.add(new_daily_score)
        db.session.commit()
        return redirect(url_for('views.leaderboard'))

    return render_template(
        "game.html",
        all_game_data_for_front_end = all_game_data_for_front_end,
        countries=countries,
        game_category_backend_names=game_category_backend_names,
        game_category_front_end_names=game_category_front_end_names,
    )


@views.route("/leaderboard", methods=["POST", "GET"])
def leaderboard():
    today = datetime.now().date()

    # find all daily scores
    todays_daily_scores = dailyScores.query.filter_by(date=today).all()
    all_daily_score_summaries = []
    for daily_score in todays_daily_scores:
        score = daily_score.score
        user_id = daily_score.user_id
        user = User.query.filter_by(id=user_id).first()
        username = user.username
        daily_score_summary = {"username": username, "score": score}
        all_daily_score_summaries.append(daily_score_summary)

    # find all-time scores
    all_users = User.query.all()
    all_user_score_summaries = []
    for user in all_users:
        username = user.username
        user_id = user.id
        all_daily_scores_for_user = dailyScores.query.filter_by(user_id=user_id).all()
        total_game_count = 0
        total_game_score = 0
        for daily_score_for_user in all_daily_scores_for_user:
            total_game_count += 1
            total_game_score += daily_score_for_user.score
        if total_game_score == 0 or total_game_count == 0:
            user_score_per_game = 0
        else:
            user_score_per_game = total_game_score/total_game_count
        user_score_summary = {
            "username": username, 
            "total_game_count": total_game_count, 
            "total_game_score": total_game_score, 
            "score_per_game": user_score_per_game
            }
        all_user_score_summaries.append(user_score_summary)
    return render_template("leaderboard.html", all_daily_score_summaries=all_daily_score_summaries, all_user_score_summaries=all_user_score_summaries)
