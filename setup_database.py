import sqlite3
import json
import os

DB_PATH = "worldcup.db"
TEAMS_JSON = "data/football.teams.json"
MATCHES_JSON = "data/football.matches.json"

def create_database():
    print("Creating database...")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        fifa_code TEXT,
        team_group TEXT 
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS matches (
        id INTEGER PRIMARY KEY,
        home_team_id INTEGER,
        away_team_id INTEGER,
        home_score INTEGER,
        away_score INTEGER,
        match_group TEXT,
        match_date TEXT,
        status TEXT,
        FOREIGN KEY (home_team_id) REFERENCES teams (id),
        FOREIGN KEY (away_team_id) REFERENCES teams (id)
    )
    """)

    with open(TEAMS_JSON, "r", encoding="utf-8") as f:
        teams_data = json.load(f)
        for team in teams_data:
            cursor.execute("""
                INSERT OR REPLACE INTO teams (id, name, fifa_code, team_group)
                VALUES (?, ?, ?, ?)""", (
                int(team["id"]),
                team["name_en"],
                team["fifa_code"],
                team["groups"]
            ))
    print(f"Successfully imported {len(teams_data)} teams!")

    with open(MATCHES_JSON, "r", encoding="utf-8") as f:
        matches_data = json.load(f)
        for match in matches_data:
            cursor.execute("""
                INSERT OR REPLACE INTO matches (id, home_team_id, away_team_id, home_score, away_score, match_group, match_date, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (
                int(match["id"]),
                int(match["home_team_id"]),
                int(match["away_team_id"]),
                int(match["home_score"]),
                int(match["away_score"]),
                match["group"],
                match["local_date"],
                match["time_elapsed"]
            ))

    print(f"Successfully imported {len(matches_data)} matches!")

    conn.commit()
    conn.close()
    print("Database created successfully and ready to use!")

if __name__ == "__main__":
    create_database()