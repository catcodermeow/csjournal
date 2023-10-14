import os
import re
import random


from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

from flask import Flask
from flask_bootstrap import Bootstrap

from flask import Flask, send_from_directory

from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# validate password to have at least 8 characters, containing uppercase letter/lowercase letter/digit/special character(#!%*)

# Configure application
app = Flask(__name__)

app.debug = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#Takes users to homepage and renders the HTML for it
@app.route("/")
@login_required
def index():
    user_id = session["user_id"]
    """Homepage to welcome users"""
    return render_template("index.html")

#code for journals webpage
@app.route("/journals", methods=["GET", "POST"])
@login_required
def journals():
    user_id = session["user_id"]

#Show list of written journal entries by date and title by selecting the database entries
    journals = db.execute("select id, title, create_date from journals where user_id = ? ", user_id)
    return render_template("journals.html", journals = journals)

#code for webpage to write a new journal entry
@app.route("/write", methods=["GET", "POST"])
@login_required
def write():
    user_id = session["user_id"]
    """Write a journal entry"""

#prompt user to enter title and journal info into form
    if request.method == "POST":
        title = request.form.get("title")
        journal = request.form.get("journal")

#return error if one field is missing
        if not title or not journal:
            return apology("Please Fill Out All Fields")

#update database by inserting new journal entry into the database
        db.execute("INSERT INTO journals (user_id, title, journal) VALUES (?, ?, ?)", user_id, title, journal)

#redisplay the new journals page with the new journal entry included
        journals = db.execute("SELECT id, title, journal, create_date FROM journals WHERE user_id = ?", user_id)
        return render_template("journals.html", journals = journals)
    else:
        return render_template("write.html")

#code for viewing individual journal entries in more detail
@app.route("/viewjournal", methods=["POST"])
@login_required
def viewjournal():

#select entire journal entry: title, date and journal entry text to display on a new subpage
    if request.method == "POST":
        journal_id = request.form.get("id")
        journal_entryDB = db.execute("SELECT * FROM journals WHERE id = ?", journal_id)
        journal_entry = journal_entryDB[0]
        return render_template("viewjournal.html", journal_entry=journal_entry)

#code for displaying all the goals and adding a new one
@app.route("/goals", methods=["GET", "POST"])
@login_required
def goals():
    user_id = session["user_id"]

#prompt user to enter a goal
    if request.method == "POST":
        goal = request.form.get("goal")

#return apology if field is not filled out
        if not goal:
            return apology("Please fill out your goal")

#update goals database to store new goal
        db.execute("INSERT INTO goals (user_id, goal) VALUES (?, ?)", user_id, goal)

#Show a list of goals
    goals = db.execute("select id, goal, date_created, date_completed, completed from goals where user_id = ? ", user_id)
    return render_template("goals.html", goals=goals)

#code for editing existing goals and marking it complete
@app.route('/edit_goal', methods=['POST'])
@login_required
def edit_goal():

#retrieve existing goal ids and prompt for a new updated goal
    user_id = session["user_id"]
    id = request.form.get("newid")
    goal = request.form.get("newgoal")

#all goals start as not complete. A goal is either completed which is assigned value (1) or not completed which is assigned value (0).
#completed goals will be marked with the date of completion by inserting into the goals database

    if request.form.get("newcompleted") != None:
        db.execute("update goals set goal = ?, completed = 1, date_completed = date() where id = ?", goal, id)
    else:
        db.execute("update goals set goal = ?, completed = 0, date_completed = null where id = ?", goal, id)

#Show list of updated goals by selecting database entries
    goals = db.execute("select id, goal, date_created, date_completed, completed from goals where user_id = ? ", user_id)
    return render_template("goals.html", goals=goals)

#code for deleting an existing goal
@app.route('/delete_goal', methods=['post'])
@login_required

#use SQL delete function to delete goal entry
def delete_goal():
    user_id = session["user_id"]
    id = request.form.get("goal_id")
    db.execute("delete from goals where id = ?", id)

#Show list of updated goals after deletion by selecting database entries
    goals = db.execute("select id, goal, date_created, date_completed, completed from goals where user_id = ? ", user_id)
    return render_template("goals.html", goals=goals)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]
        user = session["username"]
        # Redirect user to home page
        return redirect("/")
        #return render_template("index.html", user=user)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return apology("No username entered.")
        password = request.form.get("password")
        if not password:
            return apology("No password entered.")
        if not validate_password(password):
            return apology("Password is not valid, password needs to have at least 8 characters with at least one uppercase letter, one lowercase letter, one digit, and one of these special characters #!%*")
        confirmation = request.form.get("confirmation")
        if not confirmation:
            return apology("No password confirmation entered.")
        if password != confirmation:
            return apology("Passwords do not match.")

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
        except:
            return apology("Username already exists.")

        return render_template("login.html")
    else:
        return render_template("register.html")

#code for rendering inspiration page
@app.route("/inspiration", methods=["GET", "POST"])
@login_required
def inspiration():

    return render_template("inspiration.html")

def validate_password(password):
    # check password length
    if len(password) < 8:
        return False
    # check password pattern
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[#!%*])[A-Za-z\d#!%*]+$'
    if re.match(pattern, password):
        return True
    else:
        return False