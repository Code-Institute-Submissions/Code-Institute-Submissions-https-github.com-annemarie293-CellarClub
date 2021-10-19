import os
import bson
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
@app.route("/home")
def home():
    return render_template("home.html")


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

        # Create new user dictionary to add to DB
        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "dob": request.form.get("dob")
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
    users = list(mongo.db.users.find())
    user = mongo.db.users.find_one({"username": session["user"]})["username"]
    first_name = mongo.db.users.find_one({
                "username": session["user"]})["first_name"]
    
    if session["user"]:
        return render_template("profile.html",
                               user=user,
                               users=users,
                               wines=wines,
                               first_name=first_name)
    else:
        return redirect(url_for('login'))


# Function to view all wines
@app.route("/view_wines/", methods=["GET", "POST"])
def view_wines():
    wines = list(mongo.db.wines.find().sort("wine_name", 1))
    user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]

    # To calculate average rating from reviews
    average_rating = list(mongo.db.wines.aggregate(
                        [{"$unwind": "$user_reviews"},
                         {"$group": {"_id": "$_id",
                          "AverageValue": {"$avg": "$user_reviews.rating"}}}]))

    
    # To add a wine to user favourites
    if request.method == "POST":
    
        favourite = {
            "wine_name": request.form.get("wine_name").lower(),
            "grape": request.form.get("grape").lower(),
            "vintage": request.form.get("vintage").lower(),
            "country": request.form.get("country").lower(),
        }
        mongo.db.users.update_one({"_id": ObjectId(user_id)},
                                    {"$push": {"favourites": favourite}})
        flash("Wine is now added to your favourites list")
        return redirect(url_for('view_wines'))

    return render_template("wines.html", wines=wines,
                           average_rating=average_rating)


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
            "wine_img": request.form.get("wine_img"),
            "submitted_by": session["user"],
            "user_reviews": [{
                '_id': bson.objectid.ObjectId(),
                "review": request.form.get("review"),
                "rating": int(request.form.get("rating")),
                "reviewed_by": session["user"]
            }]
        }
        mongo.db.wines.insert_one(wine)
        
        flash("Your wine has been added to our collection!")
        return redirect(url_for('view_wines'))

    types = mongo.db.wine_type.find().sort("wine_type", 1)
    return render_template("add-wine.html", types=types)


# Function to add a new review to the wine
@app.route("/add_review/<wine_id>", methods=["GET", "POST"])
def add_review(wine_id):
    wine = mongo.db.wines.find_one({"_id": ObjectId(wine_id)})

    # Check if user has already reviewed this wine
    review_exists = wine["user_reviews"]
    reviewer = "unknown"

    for x in review_exists:
        if x["reviewed_by"] == session["user"]:
            reviewer = x["reviewed_by"]
        else:
            reviewer = "other"
        
    if reviewer == session["user"]:
        flash("You have already reviewed this wine, please edit your review instead")
        return redirect(url_for('view_wines'))
    
    if request.method == "POST":
        # Create new review object to add to
        # user_review array in the wine doc in wines db
        review = {
            '_id': bson.objectid.ObjectId(),
            "review": request.form.get("review"),
            "rating": int(request.form.get("rating")),
            "reviewed_by": session["user"]
        }
        mongo.db.wines.update_one({"_id": ObjectId(wine_id)},
                                  {"$push": {"user_reviews": review}})
        flash("Review successfully submitted")
        return redirect(url_for('view_wines'))

    return render_template("add-review.html", wine=wine)


# Function to edit an existing review
@app.route("/edit_review/<wine_id>", methods=["GET", "POST"])
def edit_review(wine_id):
    wine = mongo.db.wines.find_one({"_id": ObjectId(wine_id)})
    # To find the existing review details to add to form 
    existing_reviews = wine["user_reviews"]

    for x in existing_reviews:
        if x["reviewed_by"] == session["user"]:
            old_review = x["review"]
            old_rating = x["rating"]
            
    if request.method == "POST":
        # Create new review object to replace the
        # existing user review in the wine doc in wines db
        review = {
            "review": request.form.get("review"),
            "rating": int(request.form.get("rating")),
            "reviewed_by": session["user"]
        }
        mongo.db.wines.update_one({"_id": ObjectId(wine_id), "user_reviews.reviewed_by": session["user"]},   
                                  {"$set": {"user_reviews.$": review}})
        flash("Review successfully submitted")
        return redirect(url_for('view_wines'))

    return render_template("edit-review.html", wine=wine,
                           existing_reviews=existing_reviews,
                           old_review=old_review,
                           old_rating=old_rating)


# Function for Delete Review
@app.route("/delete_review/<wine_id>")
def delete_review(wine_id):
    mongo.db.wines.update({"_id": ObjectId(wine_id)}, {"$pull": {'user_reviews': {"reviewed_by": session['user']}}})

    flash("Wine review has successfully been removed")
    return redirect(url_for('view_wines'))


# Function for Delete Wine - Admin user only
@app.route("/delete_wine/<wine_id>")
def delete_wine(wine_id):
    mongo.db.wines.remove({"_id": ObjectId(wine_id)})
    flash("This wine has now been deleted from our collection")
    return redirect(url_for('view_wines'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
