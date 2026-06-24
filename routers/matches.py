from fastapi import APIRouter, HTTPException
import sqlite3

router = APIRouter(prefix="/matches", tags=["Matches"])


def get_db_connection():
    connection_db = sqlite3.connect("worldcup.db")
    connection_db.row_factory = sqlite3.Row
    return connection_db

def format_match(row):
    return {
        "id": row["id"],
        "home": row["home_name"],
        "away": row["away_name"],
        "score": {
            "home_score": row["home_score"],
            "away_score": row["away_score"]
        },
        "group": row["match_group"],
        "datetime": row["match_date"],
        "status": row["status"]
    }

@router.get("/")
async def list_matches():
    connection_db = get_db_connection()
    cursor = connection_db.cursor()
    cursor.execute("""
    SELECT m.*, th.name as home_name, ta.name as away_name
    FROM matches m
    JOIN teams th ON m.home_team_id = th.id
    JOIN teams ta ON m.away_team_id = ta.id
    """)
    matches = cursor.fetchall()
    connection_db.close()

    return {"matches": [format_match(m) for m in matches]}


@router.get("/{match_id}")
async def detail_match(match_id: int):
    connection_db = get_db_connection()
    cursor = connection_db.cursor()
    cursor.execute("""
    SELECT m.*, th.name as home_name, ta.name as away_name
    FROM matches m
    JOIN teams th ON m.home_team_id = th.id
    JOIN teams ta ON m.away_team_id = ta.id
    WHERE m.id = ?
    """, (match_id,))
    match = cursor.fetchone()
    connection_db.close()

    if not match:
        raise HTTPException(status_code=404, detail="Match not found")

    return format_match(match)

@router.get("/date/{match_date}")
async def filter_matches_by_date(match_date: str):
    connection_db = get_db_connection()
    cursor = connection_db.cursor()
    cursor.execute("""
    SELECT m.*, th.name as home_name, ta.name as away_name
    FROM matches m
    JOIN teams th ON m.home_team_id = th.id
    JOIN teams ta ON m.away_team_id = ta.id
    """)
    matches = cursor.fetchall()
    connection_db.close()

    daily_matches = []

    for m in matches:
        db_date = m["match_date"].split(" ")[0]
        try:
            month, day, year = db_date.split("/")
            formatted_db_date = f"{year}-{month}-{day}"
        except ValueError:
            formatted_db_date = db_date

        if formatted_db_date == match_date:
            daily_matches.append(format_match(m))

    if not daily_matches:
        raise HTTPException(status_code=404, detail="Match not found. Reminder: format should be YYYY-MM-DD")

    return {
        "date": match_date,
        "total_matches": len(daily_matches),
        "matches": daily_matches
    }
