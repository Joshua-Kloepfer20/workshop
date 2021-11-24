from flask import Flask,render_template
import urllib, json



app = Flask(__name__) 


@app.route('/')
def main():
    nasa = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=pJkgjfYApMvTrcMw0O7hdO7Chooqu9b4jcuDu2zC')
    nasa_text = json.load(nasa)
    return render_template('main.html', pic = nasa_text['url'], explanation = nasa_text['explanation'])


if __name__ == '__main__':
    app.debug = True
    app.run()