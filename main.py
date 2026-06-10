from fastapi import FastAPI, HTTPException
from routers import groups, matches, standings

app = FastAPI(title="World Cup API 2026")  # API title for documentation


@app.head("/")
@app.get("/")
async def home():
    return {"message": "World Cup API 2026 is running!"}


# Modules connection
app.include_router(groups.router)
app.include_router(matches.router)
app.include_router(standings.router)
