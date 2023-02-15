from flask import Blueprint, render_template

views = Blueprint(__name__, 'views')

@views.route("/")
def home():
    return render_template("home.html")
@views.route("/login")
def login():
    return render_template("login.html")
@views.route("/signup")
def signup():
    return render_template("signup.html")