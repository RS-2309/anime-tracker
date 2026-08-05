import json
from flask import Flask, render_template, request, redirect
from api import Api

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    anime = request.args.get("anime")
    results = Api.search(anime)
    return render_template('search.html', results=results)

@app.route("/anime/<int:id>")
def description(id):
    anime, studioNames = Api.getAnime(id)

    with open("json/data.json", "r") as f:
        data = json.load(f)

    is_favourite = id in data["Favourites"]

    return render_template('anime.html', anime=anime, studioNames=studioNames, id=id, is_favourite=is_favourite)

@app.route("/favourites")
def display_favourites():
    with open("json/data.json", "r") as f:
        data = json.load(f)

    favourites = [(id, Api.getAnime(id)[0]) for id in data["Favourites"]]

    return render_template('favourites.html', favourites=favourites)

@app.route("/favourites/<int:id>", methods=["POST"])
def favourite(id):
    with open("json/data.json", "r") as f:
        data = json.load(f)

    if id in data["Favourites"]:
        data["Favourites"].remove(id)
        is_favourite = False

    else:
        data["Favourites"].append(id)
        is_favourite = True

    with open("json/data.json", "w") as f:
        json.dump(data, f, indent=2)

    return {"favourite": is_favourite}

if __name__ == "__main__":
    app.run(debug=True)