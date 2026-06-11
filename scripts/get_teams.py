# Script: Query Search for different database team spelling problems

import os
import requests
from dotenv import load_dotenv

# Authenticate
load_dotenv()
api_key = os.getenv("API_FOOTBALL_KEY")

if not api_key:
    raise ValueError("API_FOOTBALL_KEY not set! Verify your .env file.")

print("\n--- API-FOOTBALL NATIONAL TEAM SEARCH ---")

team = 0
while team < 48:
    search_query = input("Enter a country name: ")
    url = f"https://v3.football.api-sports.io/teams?search={search_query}"
    headers = {"x-apisports-key": api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        teams = data.get("response", [])

        found_national_team = False
        print("\n--- RESULTS ---")

        for item in teams:
            if item["team"]["national"]:
                official_name = item["team"]["name"]
                team_id = item["team"]["id"]
                print(f"Official Spelling: '{official_name}' (ID: {team_id})")
                found_national_team = True

            if not found_national_team:
                print("No national team found. Try a different spelling.")

    else:
        print(f"Connection error: {response.status_code}")

    team += 1

""" TRUE: Mexico, South Africa, Canada, Qatar, Switzerland, Brazil, Morocco, Haiti, Scotland, USA, Paraguay, Australia,
Germany, Ecuador, Netherlands, Japan, Sweden, Tunisia, Belgium, Egypt, New Zealand, Spain, Saudi Arabia, Uruguay,
France, Senegal, Iraq, Norway, Argentina, Algeria, Austria, Jordan, Portugal, Congo DR, Uzbekistan, Colombia,
England, Croatia, Ghana, Panama."""

#FALSE: Korea Republic, Czechia, Bosnia and Herzegovina, Türkiye, Curaçao, Côte d'Ivoire, IR Iran, Cabo Verde.
