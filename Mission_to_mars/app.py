from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


@app.route("/")
def index():
    marsData = mongo.db.marsData.find_one()
    return render_template("index.html", marsData=marsData)



@app.route("/scrape")
def scraper():
    # Might need to change this to the separate data being pulled from the web
    marsData = mongo.db.marsData
    marsData_scraped = scrape_mars.scrape()
    marsData.update({}, marsData_scraped, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
