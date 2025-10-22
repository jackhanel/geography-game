from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)


class dailyChallenges(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    all_game_data_for_front_end = db.Column(db.JSON, nullable=False)
    countries = db.Column(db.JSON, nullable=False)
    game_category_backend_names = db.Column(db.JSON, nullable=False)
    game_category_front_end_names = db.Column(db.JSON, nullable=False)


class dailyScores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    score = db.Column(db.Integer, nullable=False)
