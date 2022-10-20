import requests
from flask import Flask, render_template, request

app = Flask(__name__)

URL = "http://universities.hipolabs.com/search"
COUNTRY = ""
PARAMS = {'country': COUNTRY}
RESPONSE = []


@app.route('/')
def home():
    return render_template("index.html", has_results=False)


@app.route("/search", methods=["GET", "POST"])
def search():
    global COUNTRY, PARAMS, RESPONSE
    if request.method == 'POST':
        COUNTRY = request.form['country']
        PARAMS = {'country': COUNTRY}
        RESPONSE = requests.get(url=URL, params=PARAMS)
        if len(RESPONSE.json()) > 0:
            return render_template("index.html", response=RESPONSE.json(), has_results=True)

    return render_template("index.html", has_results=False)


if __name__ == "__main__":
    app.run(debug=True)
