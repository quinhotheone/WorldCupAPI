from fastapi import FastAPI, HTTPException

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
