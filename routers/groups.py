from fastapi import APIRouter, HTTPException
from database import wc_groups

router = APIRouter(prefix="/groups", tags=["Groups"])

@router.get("/")
async def list_groups():
    return {"groups": wc_groups}


@router.get("/{group_name}")
async def detail_group(group_name: str):
    group_name = group_name.upper()

    # If there is not the searched group, the return will be a 404 error.
    if group_name not in wc_groups:
        raise HTTPException(status_code=404, detail="Group not found. Try A-L")
    return {"group": group_name, "squads": wc_groups[group_name]}