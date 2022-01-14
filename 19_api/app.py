<<<<<<< HEAD
from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

nasa = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=pJkgjfYApMvTrcMw0O7hdO7Chooqu9b4jcuDu2zC")

d = json.load(nasa.read())
print(d)



if __name__ == "__main__":
    app.debug = True
    app.run()
=======
'''
    Qina Liu, Joshua Kleopfar | Period 2
    SoftDev
    k19
    11-23-2021
    time spent: .8 hour
'''

from flask import Flask,render_template
import urllib, json



app = Flask(__name__) 


@app.route('/')
def main():
    nasa = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=pJkgjfYApMvTrcMw0O7hdO7Chooqu9b4jcuDu2zC')
    nasa_text = json.load(nasa)
    picture = (nasa_text['url']) 
    return render_template('main.html', pic = nasa_text['url'], explanation = nasa_text['explanation'])


if __name__ == '__main__':
    app.debug = True
    app.run()
>>>>>>> b066c15297a0e86a8f83d1e3b4e8030e73f189a4
