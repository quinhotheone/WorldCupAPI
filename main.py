from fastapi import FastAPI, HTTPException
from routers import groups, matches

app = FastAPI(title="World Cup API 2026")  # API title for documentation


app.include_router(matches.router) # Matches module connection
app.include_router(groups.router)

@app.head("/")
@app.get("/")
async def home():
    return {"message": "World Cup API 2026 is running!"}
