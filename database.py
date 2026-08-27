import sqlite3
from api import Api

def get_connected():
    return sqlite3.connect("data/anime.db")

def edit_favourites():
    connection = sqlite3.connect("data/anime.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id FROM favourites"
    )

    id_list = [row[0] for row in cursor.fetchall()]

    connection.close()
    
    return id_list

def remove_favourite(id):
    connection = sqlite3.connect("data/anime.db")
    cursor = connection.cursor()

    cursor.execute(
        '''DELETE FROM favourites
        WHERE id = ?;''',
        (id,)
    )

    connection.commit()
    connection.close()

def add_favourite(id):
    connection = sqlite3.connect("data/anime.db")
    cursor = connection.cursor()

    data = Api.get_data(id)

    placeholders = ",".join("?" for _ in data)

    cursor.execute(
        f'''INSERT INTO favourites
        (id, genre, score, format, episodes, season, seasonYear, status, duration, source, isAdult, start, end, studio)
        VALUES ({placeholders});''',
        data
    )

    connection.commit()
    connection.close()