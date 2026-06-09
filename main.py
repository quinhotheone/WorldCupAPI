from fastapi import FastAPI, HTTPException
from datetime import datetime, timezone

app = FastAPI(title="World Cup API 2026")  # API title for documentation

# World Cup Groups / Database
wc_groups = {
    "A": ["Mexico", "South Africa", "Korea Republic", "Czechia"],
    "B": ["Canada", "Bosnia and Herzegovina", "Qatar", "Switzerland"],
    "C": ["Brazil", "Morocco", "Haiti", "Scotland"],
    "D": ["USA", "Paraguay", "Australia", "Türkiye"],
    "E": ["Germany", "Curaçao", "Côte d'Ivoire", "Ecuador"],
    "F": ["Netherlands", "Japan", "Sweden", "Tunisia"],
    "G": ["Belgium", "Egypt", "IR Iran", "New Zealand"],
    "H": ["Spain", "Cabo Verde", "Saudi Arabia", "Uruguay"],
    "I": ["France", "Senegal", "Iraq", "Norway"],
    "J": ["Argentina", "Algeria", "Austria", "Jordan"],
    "K": ["Portugal", "Congo DR", "Uzbekistan", "Colombia"],
    "L": ["England", "Croatia", "Ghana", "Panama"]
}


@app.get("/")
async def home():
    return {"message": "World Cup API 2026 is running!"}


@app.get("/groups")
async def list_groups():
    return {"groups": wc_groups}


@app.get("/groups/{group_name}")
async def detail_group(group_name: str):
    group_name = group_name.upper()

    # If there is not the searched group, the return will be a 404 error.
    if group_name not in wc_groups:
        raise HTTPException(status_code=404, detail="Group not found. Try A-L")
    return {"group": group_name, "squads": wc_groups[group_name]}


# Stadiums Database
## Review names
wc_stadiums = {
    "MEX_AZT": "Estadio Azteca, Mexico City",
    "MEX_GUA": "Guadalajara Stadium, Guadalajara",
    "MEX_MON": "Monterrey Stadium, Monterrey",
    "CAN_TOR": "Toronto Stadium, Toronto",
    "CAN_VAN": "BC Place Vancouver, Vancouver",
    "USA_LA": "Los Angeles Stadium, Los Angeles",
    "USA_SF": "San Francisco Bay Area Stadium, San Francisco Bay Area",
    "USA_NY_NJ": "New York / New Jersey Stadium, New Jersey",
    "USA_BOS": "Boston Stadium, Boston",
    "USA_HOU": "Houston Stadium, Houston",
    "USA_DAL": "Dallas Stadium, Dallas",
    "USA_PHI": "Philadelphia Stadium, Philadelphia",



}

# Matches Database - First Phase / Group Stage Clash (MVP)
## Review datetime
wc_matches = [
    {
        "id": 1,
        "home": wc_groups["A"][0],
        "away": wc_groups["A"][1],
        "group": "A",
        "stadium": wc_stadiums["MEX_AZT"],
        "datetime": datetime(2026, 6, 11, tzinfo=timezone.utc)
    },
    {
        "id": 2,
        "home": wc_groups["A"][2],
        "away": wc_groups["A"][3],
        "group": "A",
        "stadium": wc_stadiums["MEX_GUA"],
        "datetime": datetime(2026, 6, 11, tzinfo=timezone.utc)
    },
    {
        "id": 3,
        "home": wc_groups["B"][0],
        "away": wc_groups["B"][1],
        "group": "B",
        "stadium": wc_stadiums["CAN_TOR"],
        "datetime": datetime(2026, 6, 12, tzinfo=timezone.utc)
    },
    {
        "id": 4,
        "home": wc_groups["D"][0],
        "away": wc_groups["D"][1],
        "group": "D",
        "stadium": wc_stadiums["USA_LA"],
        "datetime": datetime(2026, 6, 12, tzinfo=timezone.utc)
    },
    {
        "id": 5,
        "home": wc_groups["B"][2],
        "away": wc_groups["B"][3],
        "group": "B",
        "stadium": wc_stadiums["USA_SF"],
        "datetime": datetime(2026, 6, 13, tzinfo=timezone.utc)
    },
    {
        "id": 6,
        "home": wc_groups["C"][0],
        "away": wc_groups["C"][1],
        "group": "C",
        "stadium": wc_stadiums["USA_NY_NJ"],
        "datetime": datetime(2026, 6, 13, tzinfo=timezone.utc)
    },
    {
        "id": 7,
        "home": wc_groups["C"][2],
        "away": wc_groups["C"][3],
        "group": "C",
        "stadium": wc_stadiums["USA_BOS"],
        "datetime": datetime(2026, 6, 13, tzinfo=timezone.utc)
    },
    {
        "id": 8,
        "home": wc_groups["D"][2],
        "away": wc_groups["D"][3],
        "group": "D",
        "stadium": wc_stadiums["CAN_VAN"],
        "datetime": datetime(2026, 6, 14, tzinfo=timezone.utc)
    },
    {
        "id": 9,
        "home": wc_groups["E"][0],
        "away": wc_groups["E"][1],
        "group": "E",
        "stadium": wc_stadiums["USA_HOU"],
        "datetime": datetime(2026, 6, 14, tzinfo=timezone.utc)
    },
    {
        "id": 10,
        "home": wc_groups["F"][0],
        "away": wc_groups["F"][1],
        "group": "F",
        "stadium": wc_stadiums["USA_DAL"],
        "datetime": datetime(2026, 6, 14, tzinfo=timezone.utc)
    },
    {
        "id": 11,
        "home": wc_groups["E"][2],
        "away": wc_groups["E"][3],
        "group": "E",
        "stadium": wc_stadiums["USA_PHI"],
        "datetime": datetime(2026, 6, 14, tzinfo=timezone.utc)
    },
    {
        "id": 12,
        "home": wc_groups["F"][2],
        "away": wc_groups["F"][3],
        "group": "F",
        "stadium": wc_stadiums["MEX_MON"],
        "datetime": datetime(2026, 6, 14, tzinfo=timezone.utc)
    },
    # {
    #     15/06...
    # }
]

# wc_groups = {
#     "A": ["Mexico", "South Africa", "Korea Republic", "Czechia"],
#     "B": ["Canada", "Bosnia and Herzegovina", "Qatar", "Switzerland"],
#     "C": ["Brazil", "Morocco", "Haiti", "Scotland"],
#     "D": ["USA", "Paraguay", "Australia", "Türkiye"],
#     "E": ["Germany", "Curaçao", "Côte d'Ivoire", "Ecuador"],
#     "F": ["Netherlands", "Japan", "Sweden", "Tunisia"],
#     "G": ["Belgium", "Egypt", "IR Iran", "New Zealand"],
#     "H": ["Spain", "Cabo Verde", "Saudi Arabia", "Uruguay"],
#     "I": ["France", "Senegal", "Iraq", "Norway"],
#     "J": ["Argentina", "Algeria", "Austria", "Jordan"],
#     "K": ["Portugal", "Congo DR", "Uzbekistan", "Colombia"],
#     "L": ["England", "Croatia", "Ghana", "Panama"]
# }
@app.get("/matches")
async def list_matches():
    return {"matches": wc_matches}

@app.get("/matches/{match_id}")
async def detail_match(match_id: int):
    for match in wc_matches:
        if match["id"] == match_id:
            return match

    raise HTTPException(status_code=404, detail="Match not found")

@app.get("/matches/date/{matchdate}")
async def filter_matches_by_date(matchdate: str):

    daily_matches = []

    for match in wc_matches:
        match_date_string = match["datetime"].date().isoformat()

        if match_date_string == matchdate:
            daily_matches.append(match)

    if not daily_matches:
        raise HTTPException(status_code=404, detail="Match not found. Reminder: format should be YYYY-MM-DD")

    return {
        "date": matchdate,
        "total_matches": len(daily_matches),
        "matches": daily_matches
    }