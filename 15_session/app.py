
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html")

@app.route("/auth", methods=['GET', 'POST'])
def auth():
    '''
    Checking if the passwords are matching, perhaps we should validate it server side
    '''
    return render_template("response.html", username = request.form['username'], password = request.form['password'])


if __name__ == "__main__":
    app.debug = True
    app.run()
