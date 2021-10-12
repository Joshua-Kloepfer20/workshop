from flask import Flask, render_template
import random
import csv
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

@app.route("/occupyflaskst")
def randomJob():
        finalDict = {}
        with open('data/occupations.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    finalDict[row['Job Class']] = float(row['Percentage'])
        x = random.randint(0, 1000)
        y = 0
        for i in finalDict:
                y += finalDict[i] * 10
                if (y > x):
                        return render_template('tablified.html', foo="duoing devos", heading="duoing devos -- Joshua Kloepfer, Mark Zhu", list="List of occupations: \n" + str(list(finalDict)), chosen= "\n\nChosen Occupation: " + str(i))
                        break
def template():
    return render_template('tablified.html',foo="Team name")
if __name__ == "__main__":
    app.debug = True
    app.run()
