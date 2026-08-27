CREATE TABLE IF NOT EXISTS anime (
    id INTEGER PRIMARY KEY,
    title TEXT,
    episodes INTEGER,
    status TEXT,
    score REAL
);

CREATE TABLE IF NOT EXISTS favourites (
    id INTEGER PRIMARY KEY,
    genre TEXT,
    score REAL,
    format TEXT,
    episodes INTEGER,
    season TEXT,
    seasonYear INTEGER,
    status TEXT,
    duration INTEGER,
    source TEXT,
    isAdult BOOLEAN,
    start INTEGER,
    end INTEGER,
    studio TEXT
);