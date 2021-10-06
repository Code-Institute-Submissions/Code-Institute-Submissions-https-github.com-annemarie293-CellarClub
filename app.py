import os
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
            
        # Create new username/password dictionary to add to DB
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Add the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
        return redirect(url_for('base', username=session["user"]))

    return render_template("register.html")


@app.route("/sign_in", methods=["GET","POST"])
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
                flash("Welcome {}!".format(request.form.get("username")))
                return redirect(url_for('base', username=session["user"]))
            else:
                # If password is incorrect
                flash("Username or password is incorrect, Please try again")
                return redirect(url_for('sign_in'))
        else:
            # If user does not exist/username is incorrect
            flash("Username or password is incorrect, Please try again")
            return redirect(url_for('sign_in'))
    
    return render_template("sign-in.html")


# @app.route("/all_wines")
# def all_wines():
# wines = mongo.db.wines.find()
# return render_template("wines.html", wines=wines)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
