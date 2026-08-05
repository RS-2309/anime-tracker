# Anime Tracker

My first full-stack web application built using Flask.

It allows users to search anime through the AniList GraphQL API, view detailed information, and maintain a persistent favourites list.

## Features

- Search anime by title
- View detailed information for each anime
  - Synopsis
  - Rating
  - Genres
  - Studios
  - Format
  - Episode count
  - Release year
- Add or remove anime from favourites
- Persistent favourites stored locally using JSON
- Dynamic favourite button using JavaScript (`fetch`)
- Responsive card-based interface

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- GraphQL
- AniList API

## Project Structure

```
Anime-Tracker/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── search.html
│   ├── anime.html
│   └── favourites.html
│
├── json/
│   └── data.json
│
├── app.py
├── api.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Anime-Tracker.git
cd Anime-Tracker
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

Install the dependencies.

```bash
pip install flask requests
```

Run the application.

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## Future Improvements

- SQLite database
- User authentication
- Watchlist
- Anime recommendations
- Character information
- Relations between seasons

## Acknowledgements

- AniList GraphQL API
- Flask