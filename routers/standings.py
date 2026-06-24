from fastapi import APIRouter, HTTPException
import sqlite3

router = APIRouter(prefix="/standings", tags=["Standings"])


def get_db_connection():
    connection_db = sqlite3.connect("worldcup.db")
    connection_db.row_factory = sqlite3.Row
    return connection_db


@router.get("/")
async def get_standings():
    connection_db = get_db_connection()
    cursor = connection_db.cursor()

    # Searching for teams to create wc table
    cursor.execute("SELECT name, team_group FROM teams")
    teams = cursor.fetchall()

    standings = {}
    for team in teams:
        g = team["team_group"]
        if g not in standings:
            standings[g] = []
        standings[g].append({
            "team": team["name"],
            "points": 0,
            "played": 0,
            "wins": 0,
            "losses": 0,
            "draws": 0,
            "goals_for": 0,
            "goals_against": 0,
            "goal_difference": 0
        })

    # Search for IN PROGRESS or FULL TIME matches
    cursor.execute("""
                   SELECT m.status,
                          m.match_group,
                          m.home_score,
                          m.away_score,
                          th.name as home_name,
                          ta.name as away_name
                   FROM matches m
                            JOIN teams th ON m.home_team_id = th.id
                            JOIN teams ta ON m.away_team_id = ta.id
                   WHERE m.status != 'not_started'
                     AND m.match_group IN ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L')
    """)
    matches = cursor.fetchall()
    connection_db.close()

    for match in matches:
        group = match["match_group"]
        home_team = match["home_name"]
        away_team = match["away_name"]

        home_score = int(match["home_score"]) if ["home_score"] is not None else 0
        away_score = int(match["away_score"]) if match["away_score"] is not None else 0

        if group not in standings:
            continue

        # Look for match teams
        home_stat = next((t for t in standings[group] if t["team"] == home_team), None)
        away_stat = next((t for t in standings[group] if t["team"] == away_team), None)

        if not home_stat or not away_stat:
            continue

        # Update stats
        home_stat["played"] += 1
        away_stat["played"] += 1
        home_stat["goals_for"] += home_score
        home_stat["goals_against"] += away_score
        away_stat["goals_for"] += away_score
        away_stat["goals_against"] += home_score
        home_stat["goal_difference"] = home_stat["goals_for"] - home_stat["goals_against"]
        away_stat["goal_difference"] = away_stat["goals_for"] - away_stat["goals_against"]

        # Update group stats
        if home_score > away_score:
            home_stat["wins"] += 1
            home_stat["points"] += 3
            away_stat["losses"] += 1
        elif home_score < away_score:
            away_stat["wins"] += 1
            away_stat["points"] += 3
            home_stat["losses"] += 1
        else:
            home_stat["draws"] += 1
            away_stat["draws"] += 1
            home_stat["points"] += 1
            away_stat["points"] += 1

    # Review tiebreak criteria (points > goals_difference > goals_for)
    for group in standings:
        standings[group].sort(
            key=lambda x: (x["points"], x["goal_difference"], x["goals_for"]),
            reverse=True)

    return {"standings": standings}
