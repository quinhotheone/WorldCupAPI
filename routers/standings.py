from fastapi import APIRouter, HTTPException
from database import wc_matches, wc_groups

router = APIRouter(prefix="/standings", tags=["Standings"])

@router.get("/")
async def get_standings():

    standings = {}
    for group, teams in wc_groups.items():
        standings[group] = []
        for team in teams:
            standings[group].append({
                "team": team,
                "points": 0,
                "played": 0,
                "wins": 0,
                "losses": 0,
                "draws": 0,
                "goals_for": 0,
                "goals_against": 0,
                "goal_difference": 0
            })

    for match in wc_matches:
        if match["status"] != "NS":
            group = match["group"]
            home_team = match["home"]
            away_team = match["away"]
            home_score = match["score"]["home_score"]
            away_score = match["score"]["away_score"]

            # Look for match teams
            home_stat = next(t for t in standings[group] if t["team"] == home_team)
            away_stat = next(t for t in standings[group] if t["team"] == away_team)

            # Update matches played
            home_stat["played"] += 1
            away_stat["played"] += 1

            # Update FOR and AGAINST goals
            home_stat["goals_for"] += home_score
            home_stat["goals_against"] += away_score
            away_stat["goals_for"] += away_score
            away_stat["goals_against"] += home_score

            # Calc GD
            home_stat["goal_difference"] = home_stat["goals_for"] - home_stat["goals_against"]
            away_stat["goal_difference"] = away_stat["goals_for"] - away_stat["goals_against"]

            # Update points and stats
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
