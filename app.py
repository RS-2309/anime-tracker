'''import json
import sqlite3'''
from flask import Flask, render_template, request, redirect
from api import Api
import database as d

app = Flask(__name__)

@app.route('/')
def home():
    connection = d.get_connected()

    with open("data/anime.sql", 'r') as f:
        sql = f.read()

    connection.executescript(sql)

    connection.commit()
    connection.close()
    
    return render_template('index.html')

@app.route('/search')
def search():
    anime = request.args.get("anime")
    results = Api.search(anime)
    return render_template('search.html', results=results)

@app.route("/anime/<int:id>")
def description(id):
    anime, studioNames = Api.getAnime(id)

    connection = d.get_connected()

    cursor = connection.cursor()

    cursor.execute(
        '''SELECT 1
        FROM favourites
        WHERE id = ?''',
        (id,)
    )

    is_favourite = cursor.fetchone()

    connection.close()

    return render_template('anime.html', anime=anime, studioNames=studioNames, id=id, is_favourite=is_favourite)

@app.route("/favourites")
def display_favourites():
    connection = d.get_connected()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM favourites;"
    )
    output = cursor.fetchall()

    favourites = [(data[0], Api.getAnime(data[0])[0]) for data in output]
    
    connection.close()
    return render_template('favourites.html', favourites=favourites)

@app.route("/favourites/<int:id>", methods=["POST"])
def favourite(id):
    id_list = d.edit_favourites()

    if id in id_list:
        d.remove_favourite(id)
        is_favourite = False

    else:
        d.add_favourite(id)
        is_favourite = True

    return {"favourite": is_favourite}

@app.route("/favourites/filter/<value>")
def filter(value):
    connection = d.get_connected()
    cursor = connection.cursor()
    if value == "All":
        cursor.execute(
            "SELECT * FROM favourites"
        )
    else:
        cursor.execute(
            '''SELECT * FROM favourites
            WHERE format = ?;''',
            (value,)
        )
    output = cursor.fetchall()

    favourites = [(data[0], Api.getAnime(data[0])[0]) for data in output]
    
    connection.close()
    return render_template('favourites_inter.html', favourites=favourites)

@app.route("/favourites/sort/<value>")
def sort(value):
    connection = d.get_connected()
    cursor = connection.cursor()

    cursor.execute(
        f'''SELECT * FROM favourites
        ORDER BY {value};'''
    )

    output = cursor.fetchall()

    favourites = [(data[0], Api.getAnime(data[0])[0]) for data in output]

    connection.close()
    return render_template('favourites_inter.html', favourites=favourites)

if __name__ == "__main__":
    app.run(debug=True)