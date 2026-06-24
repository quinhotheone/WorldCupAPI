import os
import requests
import sqlite3
from dotenv import load_dotenv

# "Local name": "API name"
team_translator = {
    "Korea Republic": "South Korea",
    "Czechia": "Czech Republic",
    "Bosnia and Herzegovina": "Bosnia",
    "Türkiye": "Turkey",
    "Curaçao": "Curacao",
    "Côte d'Ivoire": "Ivory Coast",
    "IR Iran": "Iran",
    "Cabo Verde": "Cape Verde"
}

# Load environment variables and authenticate
load_dotenv()
API_KEY = os.getenv("FOOTBALL_DATA_API_KEY")
DB_PATH = "worldcup.db"

def sync_matches():
    print("Starting sync with Football-Data.org...")

    if not API_KEY:
        raise ValueError("FOOTBALL_DATA_API_KEY not set! Verify your .env file.")
        return

    # WC id=2000
    url = "https://api.football-data.org/v4/competitions/2000/matches"
    headers = {"X-Auth-Token": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error accessing the API: {e}")
        return

    data = response.json()
    matches_api = data.get("matches", [])

    if not matches_api:
        print("Matches not found!")
        return

    connection_db = sqlite3.connect(DB_PATH)
    cursor = connection_db.cursor()
    updates = 0

    for match in matches_api:
        status = match.get("status")
        home_team_api = match.get("homeTeam", {})
        away_team_api = match.get("awayTeam", {})
        score = match.get("score", {}).get("fullTime", {})

        home_code = home_team_api.get("tla")
        away_code = away_team_api.get("tla")
        home_goals = score.get("home")
        away_goals = score.get("away")

        if not home_code or not away_code or home_goals is None or away_goals is None:
            continue

        cursor.execute("""
        SELECT m.id, m.home_score, m.away_score
        FROM matches m
        JOIN teams th ON m.home_team_id = th.id
        JOIN teams ta ON m.away_team_id = ta.id
        WHERE th.fifa_code = ? AND ta.fifa_code = ?
        """, (home_code, away_code))

        db_match = cursor.fetchone()

        if db_match:
            match_id, db_home_score, db_away_score = db_match

            # Verifying updates
            if db_home_score != home_goals or db_away_score != away_goals:
                cursor.execute("""
                UPDATE matches
                SET home_score = ?, away_score = ?, status = ?
                WHERE id = ?
                """, (home_goals, away_goals, status, match_id))
                updates += 1
                print(f"It is a GOAL! {home_code} {home_goals} x {away_goals} {away_code}")

    if updates > 0:
        connection_db.commit()
        print(f"Sync complete! Successfully updated for {updates} matches in database.")
    else:
        print("Sync complete. No updates needed for now!")

    connection_db.close()

if __name__ == "__main__":
    sync_matches()

