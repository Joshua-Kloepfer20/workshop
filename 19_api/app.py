from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

nasa = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=pJkgjfYApMvTrcMw0O7hdO7Chooqu9b4jcuDu2zC")

d = json.load(nasa.read())
print(d)



if __name__ == "__main__":
    app.debug = True
    app.run()
