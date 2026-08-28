# Anime Tracker

My first full-stack web application built using Flask.

Anime Tracker allows users to search anime through the AniList GraphQL API, view detailed information, and maintain a persistent favourites list using a local SQLite database.

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
- Persistent favourites stored locally using SQLite
- Dynamic favourite button using JavaScript (`fetch`)
- Filter favourites by anime format
- Sort favourites by:
  - Name (A-Z / Z-A)
  - Episode count (Low to High / High to Low)
  - Score (Low to High / High to Low)
  - Release year (Oldest to Newest / Newest to Oldest)
- Responsive card-based interface

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- GraphQL
- AniList API

## Project Structure

```text
Anime-Tracker/

│
├── data/
│   ├── anime.db
│   └── anime.sql
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
│   ├── favourites.html
│   └── favourites_inter.html
│
├── app.py
├── api.py
├── database.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Anime-Tracker.git

cd Anime-Tracker
```

Create a virtual environment:

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

Install the dependencies:

```bash
pip install flask requests
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Database

Anime Tracker uses **SQLite** to persist favourite anime data locally.

The database stores information such as:

- Anime ID
- Title
- Genres
- Score
- Format
- Episode count
- Season
- Release year
- Status
- Duration
- Source
- Studio information

## Future Improvements

- User authentication
- Watchlist
- Anime recommendations
- Character information
- Relations between seasons
- Genre filtering
- Improved caching for API requests

## Acknowledgements

- AniList GraphQL API
- Flask
