from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from .models import User
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            password = request.form.get("password")
            if check_password_hash(existing_user.password, password):
                flash("Logged in successfully", category="success")
                login_user(existing_user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash(f"The password you have entered does not match the password we have stored for '{username}'.", category="error")
        else:
            flash(f"The username '{username}' does not exist in our database. Please create an account.", category="error")
            return redirect(url_for("auth.createAccount"))
    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/create-account", methods=["POST", "GET"])
def createAccount():
    if request.method == "POST":
        username = request.form.get("username")
        existing_user = User.query.filter_by(username=username).first()
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        if existing_user:
            flash(f"The username '{username}' already exists in our database. Please log in to your account.", category="error")
            return redirect(url_for("auth.login"))
        elif len(password1) < 8:
            flash("Your password must be 8 or more characters in length.", category="error")
        elif password1 != password2:
            flash("The passwords you have entered do not match.", category="error")
        else:
            new_user = User(
                username=username,
                password=generate_password_hash(password1, method="scrypt"),
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Your account has been created!", category="success")
            return redirect(url_for("views.home"))

    return render_template("create_account.html", user=current_user)
