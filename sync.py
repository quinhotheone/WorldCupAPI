import os
import requests
from dotenv import load_dotenv

from database import wc_matches

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
api_key = os.getenv("API_FOOTBALL_KEY")

if not api_key:
    raise ValueError("API_FOOTBALL_KEY not set! Verify your .env file.")

url = "https://v3.football.api-sports.io/fixtures?league=1&season=2026"
headers = {"x-apisports-key": api_key}

print("Starting background sync with API-Football...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    live_matches = data.get("response", [])

    update_count = 0

    for live_match in live_matches:
        api_home_team = live_match["teams"]["home"]["name"]
        api_away_team = live_match["teams"]["away"]["name"]
        api_status = live_match["fixture"]["status"]["short"]
        api_home_goals = live_match["goals"]["home"]
        api_away_goals = live_match["goals"]["away"]

        for local_match in wc_matches:

            local_home_translated = team_translator.get(local_match["home"], local_match["home"])
            local_away_translated = team_translator.get(local_match["away"], local_match["away"])

            if local_home_translated == api_home_team and local_away_translated == api_away_team:

                local_match["status"] = api_status

                if api_home_goals is not None and api_away_goals is not None:
                    local_match["score"]["home_score"] = api_home_goals
                    local_match["score"]["away_score"] = api_away_goals

                update_count += 1
                break

    print(f"Sync complete! Successfully updated for {update_count} matches.")

    print(f"\n--- ALL LOCAL MATCHES STATUS REPORT ---")
    for match in wc_matches:
        status_icon = "⚪" if match["status"] == "FT" else "🟢" if match["status"] == "1H" or match[
            "status"] == "2H" else "🔵"
        home_score = match["score"]["home_score"]
        away_score = match["score"]["away_score"]

        print(
            f"{status_icon} [{match['status']}] {match['home']} {home_score} - {away_score} {match['away']} (Group {match['group']})")

else:
    print(f"Connection error: {response.status_code}")
