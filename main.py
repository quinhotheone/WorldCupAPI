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


@app.head("/")
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
    "USA_ATL": "Atlanta Stadium, Atlanta",
    "USA_SEA": "Seattle Stadium, Seattle",
    "USA_MIA": "Miami Stadium, Miami",
    "USA_KAN": "Kansas City Stadium, Kansas City",
}

# Matches Database - First Phase / Group Stage Clash (MVP)
## Review teams and datetime
wc_matches = [
    {
        "id": 1,
        "home": wc_groups["A"][0],
        "away": wc_groups["A"][1],
        "group": "A",
        "stadium": wc_stadiums["MEX_AZT"],
        "datetime": datetime(2026, 6, 11, tzinfo=timezone.utc),
        "score": {"home_score": 1, "away_score": 0},
        "status": "1H"
    },
    {
        "id": 2,
        "home": wc_groups["A"][2],
        "away": wc_groups["A"][3],
        "group": "A",
        "stadium": wc_stadiums["MEX_GUA"],
        "datetime": datetime(2026, 6, 11, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 3,
        "home": wc_groups["B"][0],
        "away": wc_groups["B"][1],
        "group": "B",
        "stadium": wc_stadiums["CAN_TOR"],
        "datetime": datetime(2026, 6, 12, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 4,
        "home": wc_groups["D"][0],
        "away": wc_groups["D"][1],
        "group": "D",
        "stadium": wc_stadiums["USA_LA"],
        "datetime": datetime(2026, 6, 12, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 5,
        "home": wc_groups["B"][2],
        "away": wc_groups["B"][3],
        "group": "B",
        "stadium": wc_stadiums["USA_SF"],
        "datetime": datetime(2026, 6, 13, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 6,
        "home": wc_groups["C"][0],
        "away": wc_groups["C"][1],
        "group": "C",
        "stadium": wc_stadiums["USA_NY_NJ"],
        "datetime": datetime(2026, 6, 13, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 7,
        "home": wc_groups["C"][2],
        "away": wc_groups["C"][3],
        "group": "C",
        "stadium": wc_stadiums["USA_BOS"],
        "datetime": datetime(2026, 6, 13, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 8,
        "home": wc_groups["D"][2],
        "away": wc_groups["D"][3],
        "group": "D",
        "stadium": wc_stadiums["CAN_VAN"],
        "datetime": datetime(2026, 6, 14, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 9,
        "home": wc_groups["E"][0],
        "away": wc_groups["E"][1],
        "group": "E",
        "stadium": wc_stadiums["USA_HOU"],
        "datetime": datetime(2026, 6, 14, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 10,
        "home": wc_groups["F"][0],
        "away": wc_groups["F"][1],
        "group": "F",
        "stadium": wc_stadiums["USA_DAL"],
        "datetime": datetime(2026, 6, 14, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 11,
        "home": wc_groups["E"][2],
        "away": wc_groups["E"][3],
        "group": "E",
        "stadium": wc_stadiums["USA_PHI"],
        "datetime": datetime(2026, 6, 14, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 12,
        "home": wc_groups["F"][2],
        "away": wc_groups["F"][3],
        "group": "F",
        "stadium": wc_stadiums["MEX_MON"],
        "datetime": datetime(2026, 6, 14, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 13,
        "home": wc_groups["H"][0],
        "away": wc_groups["H"][1],
        "group": "H",
        "stadium": wc_stadiums["USA_ATL"],
        "datetime": datetime(2026, 6, 15, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 14,
        "home": wc_groups["G"][0],
        "away": wc_groups["G"][1],
        "group": "G",
        "stadium": wc_stadiums["USA_SEA"],
        "datetime": datetime(2026, 6, 15, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 15,
        "home": wc_groups["H"][2],
        "away": wc_groups["H"][3],
        "group": "H",
        "stadium": wc_stadiums["USA_MIA"],
        "datetime": datetime(2026, 6, 15, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 16,
        "home": wc_groups["G"][2],
        "away": wc_groups["G"][3],
        "group": "G",
        "stadium": wc_stadiums["USA_LA"],
        "datetime": datetime(2026, 6, 15, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 17,
        "home": wc_groups["I"][0],
        "away": wc_groups["I"][1],
        "group": "I",
        "stadium": wc_stadiums["USA_NY_NJ"],
        "datetime": datetime(2026, 6, 16, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 18,
        "home": wc_groups["I"][2],
        "away": wc_groups["I"][3],
        "group": "I",
        "stadium": wc_stadiums["USA_BOS"],
        "datetime": datetime(2026, 6, 16, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 19,
        "home": wc_groups["J"][0],
        "away": wc_groups["J"][1],
        "group": "J",
        "stadium": wc_stadiums["USA_KAN"],
        "datetime": datetime(2026, 6, 16, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 20,
        "home": wc_groups["J"][2],
        "away": wc_groups["J"][3],
        "group": "J",
        "stadium": wc_stadiums["USA_SF"],
        "datetime": datetime(2026, 6, 17, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 21,
        "home": wc_groups["K"][0],
        "away": wc_groups["K"][1],
        "group": "K",
        "stadium": wc_stadiums["USA_HOU"],
        "datetime": datetime(2026, 6, 17, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 22,
        "home": wc_groups["L"][0],
        "away": wc_groups["L"][1],
        "group": "L",
        "stadium": wc_stadiums["USA_DAL"],
        "datetime": datetime(2026, 6, 17, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 23,
        "home": wc_groups["L"][2],
        "away": wc_groups["L"][3],
        "group": "L",
        "stadium": wc_stadiums["CAN_TOR"],
        "datetime": datetime(2026, 6, 17, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 24,
        "home": wc_groups["K"][2],
        "away": wc_groups["K"][3],
        "group": "K",
        "stadium": wc_stadiums["MEX_AZT"],
        "datetime": datetime(2026, 6, 15, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 25,
        "home": wc_groups["A"][3],
        "away": wc_groups["A"][1],
        "group": "A",
        "stadium": wc_stadiums["USA_ATL"],
        "datetime": datetime(2026, 6, 18, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 26,
        "home": wc_groups["B"][3],
        "away": wc_groups["B"][1],
        "group": "B",
        "stadium": wc_stadiums["USA_LA"],
        "datetime": datetime(2026, 6, 18, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 27,
        "home": wc_groups["B"][0],
        "away": wc_groups["B"][2],
        "group": "B",
        "stadium": wc_stadiums["CAN_VAN"],
        "datetime": datetime(2026, 6, 18, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 28,
        "home": wc_groups["A"][0],
        "away": wc_groups["A"][2],
        "group": "A",
        "stadium": wc_stadiums["MEX_GUA"],
        "datetime": datetime(2026, 6, 18, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 29,
        "home": wc_groups["D"][0],
        "away": wc_groups["D"][2],
        "group": "D",
        "stadium": wc_stadiums["USA_SEA"],
        "datetime": datetime(2026, 6, 19, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 30,
        "home": wc_groups["C"][3],
        "away": wc_groups["C"][1],
        "group": "C",
        "stadium": wc_stadiums["USA_BOS"],
        "datetime": datetime(2026, 6, 19, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 31,
        "home": wc_groups["C"][0],
        "away": wc_groups["C"][2],
        "group": "C",
        "stadium": wc_stadiums["USA_PHI"],
        "datetime": datetime(2026, 6, 19, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 32,
        "home": wc_groups["D"][3],
        "away": wc_groups["D"][1],
        "group": "D",
        "stadium": wc_stadiums["USA_SF"],
        "datetime": datetime(2026, 6, 20, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 33,
        "home": wc_groups["F"][0],
        "away": wc_groups["F"][2],
        "group": "F",
        "stadium": wc_stadiums["USA_HOU"],
        "datetime": datetime(2026, 6, 20, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 34,
        "home": wc_groups["E"][0],
        "away": wc_groups["E"][2],
        "group": "E",
        "stadium": wc_stadiums["CAN_TOR"],
        "datetime": datetime(2026, 6, 20, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 35,
        "home": wc_groups["E"][3],
        "away": wc_groups["E"][1],
        "group": "E",
        "stadium": wc_stadiums["USA_KAN"],
        "datetime": datetime(2026, 6, 20, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 36,
        "home": wc_groups["F"][3],
        "away": wc_groups["F"][1],
        "group": "F",
        "stadium": wc_stadiums["MEX_MON"],
        "datetime": datetime(2026, 6, 21, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 37,
        "home": wc_groups["H"][0],
        "away": wc_groups["H"][2],
        "group": "H",
        "stadium": wc_stadiums["USA_ATL"],
        "datetime": datetime(2026, 6, 21, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 38,
        "home": wc_groups["G"][0],
        "away": wc_groups["G"][2],
        "group": "G",
        "stadium": wc_stadiums["USA_LA"],
        "datetime": datetime(2026, 6, 21, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 39,
        "home": wc_groups["H"][3],
        "away": wc_groups["H"][1],
        "group": "H",
        "stadium": wc_stadiums["USA_MIA"],
        "datetime": datetime(2026, 6, 21, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 40,
        "home": wc_groups["G"][3],
        "away": wc_groups["G"][1],
        "group": "G",
        "stadium": wc_stadiums["CAN_VAN"],
        "datetime": datetime(2026, 6, 21, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 41,
        "home": wc_groups["J"][0],
        "away": wc_groups["J"][2],
        "group": "J",
        "stadium": wc_stadiums["USA_DAL"],
        "datetime": datetime(2026, 6, 22, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 42,
        "home": wc_groups["I"][0],
        "away": wc_groups["I"][2],
        "group": "I",
        "stadium": wc_stadiums["USA_PHI"],
        "datetime": datetime(2026, 6, 22, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 43,
        "home": wc_groups["I"][3],
        "away": wc_groups["I"][1],
        "group": "I",
        "stadium": wc_stadiums["USA_NY_NJ"],
        "datetime": datetime(2026, 6, 22, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 44,
        "home": wc_groups["J"][3],
        "away": wc_groups["J"][1],
        "group": "J",
        "stadium": wc_stadiums["USA_SF"],
        "datetime": datetime(2026, 6, 23, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 45,
        "home": wc_groups["K"][0],
        "away": wc_groups["K"][2],
        "group": "K",
        "stadium": wc_stadiums["USA_HOU"],
        "datetime": datetime(2026, 6, 23, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 46,
        "home": wc_groups["L"][0],
        "away": wc_groups["L"][2],
        "group": "L",
        "stadium": wc_stadiums["USA_BOS"],
        "datetime": datetime(2026, 6, 23, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 47,
        "home": wc_groups["L"][3],
        "away": wc_groups["L"][1],
        "group": "L",
        "stadium": wc_stadiums["CAN_TOR"],
        "datetime": datetime(2026, 6, 23, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 48,
        "home": wc_groups["K"][3],
        "away": wc_groups["K"][1],
        "group": "K",
        "stadium": wc_stadiums["MEX_GUA"],
        "datetime": datetime(2026, 6, 23, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 49,
        "home": wc_groups["B"][3],
        "away": wc_groups["B"][0],
        "group": "B",
        "stadium": wc_stadiums["CAN_VAN"],
        "datetime": datetime(2026, 6, 24, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 50,
        "home": wc_groups["B"][1],
        "away": wc_groups["B"][2],
        "group": "B",
        "stadium": wc_stadiums["USA_SEA"],
        "datetime": datetime(2026, 6, 24, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 51,
        "home": wc_groups["C"][3],
        "away": wc_groups["C"][0],
        "group": "C",
        "stadium": wc_stadiums["USA_MIA"],
        "datetime": datetime(2026, 6, 24, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 52,
        "home": wc_groups["C"][1],
        "away": wc_groups["C"][2],
        "group": "C",
        "stadium": wc_stadiums["USA_ATL"],
        "datetime": datetime(2026, 6, 24, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 53,
        "home": wc_groups["A"][3],
        "away": wc_groups["A"][0],
        "group": "A",
        "stadium": wc_stadiums["MEX_AZT"],
        "datetime": datetime(2026, 6, 24, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 54,
        "home": wc_groups["A"][1],
        "away": wc_groups["A"][2],
        "group": "A",
        "stadium": wc_stadiums["MEX_MON"],
        "datetime": datetime(2026, 6, 24, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 55,
        "home": wc_groups["E"][1],
        "away": wc_groups["E"][2],
        "group": "E",
        "stadium": wc_stadiums["USA_PHI"],
        "datetime": datetime(2026, 6, 25, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 56,
        "home": wc_groups["E"][3],
        "away": wc_groups["E"][0],
        "group": "E",
        "stadium": wc_stadiums["USA_NY_NJ"],
        "datetime": datetime(2026, 6, 25, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 57,
        "home": wc_groups["F"][3],
        "away": wc_groups["F"][0],
        "group": "F",
        "stadium": wc_stadiums["USA_KAN"],
        "datetime": datetime(2026, 6, 25, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 58,
        "home": wc_groups["D"][3],
        "away": wc_groups["D"][0],
        "group": "D",
        "stadium": wc_stadiums["USA_LA"],
        "datetime": datetime(2026, 6, 25, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 59,
        "home": wc_groups["D"][1],
        "away": wc_groups["D"][2],
        "group": "D",
        "stadium": wc_stadiums["USA_SF"],
        "datetime": datetime(2026, 6, 23, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 60,
        "home": wc_groups["I"][3],
        "away": wc_groups["I"][0],
        "group": "I",
        "stadium": wc_stadiums["USA_BOS"],
        "datetime": datetime(2026, 6, 26, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 61,
        "home": wc_groups["I"][1],
        "away": wc_groups["I"][2],
        "group": "I",
        "stadium": wc_stadiums["CAN_TOR"],
        "datetime": datetime(2026, 6, 26, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 62,
        "home": wc_groups["H"][1],
        "away": wc_groups["H"][2],
        "group": "H",
        "stadium": wc_stadiums["USA_HOU"],
        "datetime": datetime(2026, 6, 26, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 63,
        "home": wc_groups["H"][3],
        "away": wc_groups["H"][0],
        "group": "H",
        "stadium": wc_stadiums["MEX_GUA"],
        "datetime": datetime(2026, 6, 26, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 64,
        "home": wc_groups["G"][1],
        "away": wc_groups["G"][2],
        "group": "G",
        "stadium": wc_stadiums["USA_SEA"],
        "datetime": datetime(2026, 6, 27, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 65,
        "home": wc_groups["G"][3],
        "away": wc_groups["G"][0],
        "group": "G",
        "stadium": wc_stadiums["CAN_VAN"],
        "datetime": datetime(2026, 6, 27, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 66,
        "home": wc_groups["L"][3],
        "away": wc_groups["L"][0],
        "group": "L",
        "stadium": wc_stadiums["USA_NY_NJ"],
        "datetime": datetime(2026, 6, 27, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 67,
        "home": wc_groups["L"][1],
        "away": wc_groups["L"][2],
        "group": "L",
        "stadium": wc_stadiums["USA_PHI"],
        "datetime": datetime(2026, 6, 27, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 68,
        "home": wc_groups["K"][3],
        "away": wc_groups["K"][0],
        "group": "K",
        "stadium": wc_stadiums["USA_MIA"],
        "datetime": datetime(2026, 6, 27, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 69,
        "home": wc_groups["K"][1],
        "away": wc_groups["K"][2],
        "group": "K",
        "stadium": wc_stadiums["USA_ATL"],
        "datetime": datetime(2026, 6, 27, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 70,
        "home": wc_groups["J"][1],
        "away": wc_groups["J"][2],
        "group": "J",
        "stadium": wc_stadiums["USA_KAN"],
        "datetime": datetime(2026, 6, 27, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    },
    {
        "id": 71,
        "home": wc_groups["J"][3],
        "away": wc_groups["J"][0],
        "group": "J",
        "stadium": wc_stadiums["USA_DAL"],
        "datetime": datetime(2026, 6, 23, tzinfo=timezone.utc),
        "score": {"home_score": 0, "away_score": 0},
        "status": "NS"
    }
]

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


match_status = {
    "NS": "Not Started",
    "1H": "First Half",
    "HT": "Half Time",
    "2H": "Second Half",
    "1HE": "First Half Extra Time",
    "HET": "Half Extra Time",
    "2HE": "Second Half Extra Time",
    "PS": "Penalty Shootout",
    "FT": "Full Time"
}
