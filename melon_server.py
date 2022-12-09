"""Server for the Melon Tasting Reservations App"""
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

from datetime import date, timedelta, datetime

app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined

###-----------------------------------HOMEPAGE--------------------------------###
@app.route('/')
def homepage():
    """"Return render template to homepage.html"""

    return render_template('home.html')

###-----------------------------------LOGIN-PAGE--------------------------------###

@app.route('/login')
def show_login_page():
    """Shows log in and create account page"""

    return render_template('login.html')


###----------------------------WHEN-USER-TRIES-TO-LOGIN-------------------------###
@app.route('/login', methods=['POST'])
def login_user():
    """Login to user account"""

    username = request.form.get("username")
    password = request.form.get("password")

    match = crud.check_email_and_pass(email, password)

    if not match:
        flash("This email doesn't match anything in our system.")
        return redirect("/login")
    else:
        session["user_id"]=match.user_id
        flash("Welcome 🍈")
        return redirect(f"/user_profile")


###----------------------------LOG-OUT--------------------------------###
@app.route('/logout')
def logout_user():
    """Log out user"""
    
    del session["user_id"]

    flash("See you next time! 🍉")

    return redirect("/login")

###----------------------------ADDING-NEW-USER-TO-DB-------------------------###
@app.route('/user_profile', methods=['POST'])
def create_new_user():
    """Create new user account"""

    username = request.form.get("username")
    password = request.form.get("password")

    user = crud.get_user_by_email(username)

    if user:
        flash("An account with this email already exists.")
    else:
        user = crud.create_user(username, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully. Please log in.")
    
        return redirect("/login")

###----------------------------USER-PROFILE-----------------------------###
@app.route('/reserve')
def show_user_profile():
    """Return render template to reserve.html"""

    if "user_id" in session:
        user = crud.get_user_by_id(session["user_id"])

        return render_template('reserve.html', user=user)

    else:
        flash("Please log in or create new account.")
        return redirect("/login")

###-----------------------------OTHER-STUFF----------------------------###

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0")   