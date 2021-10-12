import os
from datetime import date, datetime
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Gets user submitted inputs from register.html
        checks if there is existing user, and
        if user is over 18. If conditions are met,
        user details are added to 'users' DB """
    if request.method == "POST":
        # Check if user already exists in DB
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            flash("Username already exists")
            return redirect(url_for('register'))

        # Check if passwords are matching
        password1 = request.form.get("password")
        password2 = request.form.get("password-check")

        if password1 != password2:
            flash("Passwords do not match, please re-check")
            return redirect(url_for('register'))

        # Check if user is over 18
        dob = request.form.get("dob")
        dob_date = datetime.strptime(dob, '%Y-%m-%d').date()
        today = date.today()
        # To Calcuate user age from dob input
        # Source: https://www.geeksforgeeks.org/
        # python-program-to-calculate-age-in-year/
        age = today.year - dob_date.year - ((
            today.month, today.day) < (dob_date.month, dob_date.day))

        if age < 18:
            flash("Sorry, You must be of legal age to join our club")
            return redirect(url_for('register'))

        # Create new username/password dictionary to add to DB
        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first-name": request.form.get("first-name").lower(),
            "last-name": request.form.get("last-name").lower(),
            "dob": request.form.get("dob"),
            "country": request.form.get("country").lower(),
        }
        mongo.db.users.insert_one(new_user)

        # Add the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
        return redirect(url_for('profile', username=session["user"]))

    return render_template("register.html")


# Function to Sign-In
@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        # Check if user already exists in DB
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            # Check password is correct
            if check_password_hash(user_exists["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}!".format(request.form.get(
                    "username").title()))
                return redirect(url_for('profile', username=session["user"]))
            else:
                # If password is incorrect
                flash("Username or password is incorrect, Please try again")
                return redirect(url_for('sign_in'))
        else:
            # If user does not exist/username is incorrect
            flash("Username or password is incorrect, Please try again")
            return redirect(url_for('sign_in'))

    return render_template("sign-in.html")


# Function to Sign Out
@app.route("/sign_out")
def sign_out():
    # Clear the session user cookie
    flash("You have been Logged out")
    session.pop("user")
    return redirect(url_for('sign_in'))


# Function to view Profile page
@app.route("/profile")
def profile():
    wines = list(mongo.db.wines.find())
    # Grab the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    first_name = mongo.db.users.find_one(
        {"first-name": session["user"]})["first-name"]

    if session["user"]:
        return render_template("profile.html",
                               username=username,
                               wines=wines,
                               first_name=first_name)
    else:
        return redirect(url_for('login'))


# Function to view all wines
@app.route("/view_wines")
def view_wines():
    wines = mongo.db.wines.find().sort("wine_name", 1)
    return render_template("wines.html", wines=wines)


# Function to add a new wine to the DB
@app.route("/add_wine", methods=["GET", "POST"])
def add_wine():
    if request.method == "POST":
        # Check if wine and vintage pair already exists in DB
        wine_exists = mongo.db.wines.find_one(
                      {"wine_name": request.form.get("wine_name").lower()})
        
        if wine_exists:
            vintage_exists = mongo.db.wines.find_one(
                             {"vintage": request.form.get("vintage")})
            if vintage_exists:
                flash("Wine/Vintage already exists, please add a review")
                return redirect(url_for("view_wines"))
        
        # Create new wine dictionary to add to DB
        wine = {
            "wine_type": request.form.get("wine_type"),
            "wine_name": request.form.get("wine_name").lower(),
            "grape": request.form.get("grape").lower(),
            "vintage": request.form.get("vintage").lower(),
            "country": request.form.get("country").lower(),
            "region": request.form.get("region").lower(),
            "submitted_by": session["user"]
        }
        mongo.db.wines.insert_one(wine)
        flash("Your wine has been added to our collection!")
        return redirect(url_for('view_wines'))

    types = mongo.db.wine_type.find().sort("wine_type", 1)
    return render_template("add-wine.html", types=types)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
