from flask import Flask, render_template
import random
import csv
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

@app.route("/occupyflaskst")
def test_tmplt():
    return render_template('tablified.html', foo="Hello")
def randomJob(reader):
       finalDict = {}
       with open('data/occupations.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                        finalDict[row['Job Class']] = float(row['Percentage'])
        x = random.randint(0, 1000)
        y = 0
        for i in reader:
                y += reader[i] * 10
                if (y > x):
                        return ("The Best Team -- Alif Abdullah, Andrew Juang, Joshua Kloepfer <br><br>List of occupations: <br>" + finalDict+ "<br><br>Chosen Occupation: " + str(finalDict))
                        break
if __name__ == "__main__":
    app.debug = True
    app.run()
