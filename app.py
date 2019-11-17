import json

from flask import Flask

from weatherapp import weather


app = Flask(__name__)

@app.route("/")
def hello():
    return  "Hello Word"

@app.route("/weather/")
def vreme():
    temp = weather.weather()
    temp = json.dumps(weather())
    return temp

@app.route("/weather/my_cities/")
def vreme_multiplecities ():
    return "Cluj: 15, New York: 20"