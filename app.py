from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# create route that renders index.html template
@app.route("/")
def index():
    mars_dic = mongo.db.mars_dic.find_one()
    return render_template("index.html", mars_dic=mars_dic)


@app.route("/scrape")
def scraper():
    mars_dic = mongo.db.mars_dic
    mars_dic_data = scrape_mars.scrape()
    print(mars_dic_data)
    print("mar_data")
    mars_dic.update({}, mars_dic_data, upsert=True)
    return redirect("/", code=302)





if __name__ == "__main__":
    app.run(debug=True)