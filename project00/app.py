from flask import Flask, render_template, request, session
import os

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    if 'username' in session.keys() and 'password' in session.keys():
        if session['username'] == USERNAME and session['password'] == PASSWORD:
            #only if the code was right will we send them to success.html
            return render_template("success.html", 
                username = session['username'], 
                password = session['password'])
        
    return render_template("login.html")
if __name__ == "__main__":
    app.debug = True
    app.run()
