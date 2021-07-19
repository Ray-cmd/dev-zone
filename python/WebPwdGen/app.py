from flask import Flask, render_template, url_for
from libs.pwdGen.pwdGen import PwdGen

app = Flask(__name__)

passwords = ("asdasdafgr", "a65sd4f6as4f4asd", "3as54d65as4d")

@app.route("/")
def home():
    return render_template("home.html", passwords = passwords)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)