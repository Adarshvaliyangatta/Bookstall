from flask import Flask, render_template
from utils.analysis import get_analysis, create_chart
import json

app = Flask(__name__)

# Load Bookstall data
def load_Bookstall():
    try:
        with open("data/Bookstall.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print(e)
        return []

@app.route("/")
def home():
    Bookstall = load_Bookstall()
    return render_template("index.html", Bookstall=Bookstall)

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/analytics")
def analytics():
    create_chart()
    result = get_analysis()
    return render_template("analytics.html", result=result)

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

if __name__ == "__main__":
    app.run(debug=True)