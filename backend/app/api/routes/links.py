from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from random import randint

from app.db.requests import add_link, get_link_by_shortcode, search_link_by_url
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.db.session import get_db

from app.services.encoding import encoding_base52, decoding_base52

router = APIRouter()

@router.get("/{code}")
async def redirect(code: str, db: AsyncSession = Depends(get_db)):
    id = decoding_base52(code)
    link_field = await get_link_by_shortcode(db, id)

    if link_field:
        return RedirectResponse(link_field.original_url, 302)
    else:
        return {"status": 404}
    

@router.post("/create")
async def create_link(url: str, db: AsyncSession = Depends(get_db)):
    double_link = await search_link_by_url(db, url)
    if double_link:
        code = encoding_base52(double_link.id)
    else:
        link_field = await add_link(db, url)
        code = encoding_base52(link_field.id)
    return {"status": 200, "link": f"http://192.168.0.12:8000/{code}"}
