from fastapi import APIRouter, HTTPException
import sqlite3

router = APIRouter(prefix="/groups", tags=["Groups"])


def get_db_connection():
    connection_db = sqlite3.connect("worldcup.db")
    connection_db.row_factory = sqlite3.Row
    return connection_db
@router.get("/")
async def list_groups():
    connection_db = get_db_connection()
    cursor = connection_db.cursor()
    cursor.execute("SELECT name, team_group FROM teams")
    teams = cursor.fetchall()
    connection_db.close()

    wc_groups = {}
    for team in teams:
        g = team["team_group"]
        if g not in wc_groups:
            wc_groups[g] = []
        wc_groups[g].append(team["name"])

    return {"groups": wc_groups}


@router.get("/{group_name}")
async def detail_group(group_name: str):
    group_name = group_name.upper()
    connection_db = get_db_connection()
    cursor = connection_db.cursor()
    cursor.execute("SELECT name FROM teams WHERE team_group = ?", (group_name,))
    teams = cursor.fetchall()
    connection_db.close()

    # If there is not the searched group, the return will be a 404 error.
    if not teams:
        raise HTTPException(status_code=404, detail="Group not found. Try A-L")

    return {"group": group_name, "squads": [t["name"] for t in teams]}