from fastapi import APIRouter, HTTPException
from database import wc_matches

router = APIRouter(prefix="/matches", tags=["Matches"])


@router.get("/")
async def list_matches():
    return {"matches": wc_matches}


@router.get("/{match_id}")
async def detail_match(match_id: int):
    for match in wc_matches:
        if match["id"] == match_id:
            return match

    raise HTTPException(status_code=404, detail="Match not found")


@router.get("/date/{match_date}")
async def filter_matches_by_date(match_date: str):

    daily_matches = []

    for match in wc_matches:
        match_date_string = match["datetime"].date().isoformat()

        if match_date_string == match_date:
            daily_matches.append(match)

    if not daily_matches:
        raise HTTPException(status_code=404, detail="Match not found. Reminder: format should be YYYY-MM-DD")

    return {
        "date": match_date,
        "total_matches": len(daily_matches),
        "matches": daily_matches
    }
