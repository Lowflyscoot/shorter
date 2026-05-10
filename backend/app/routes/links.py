import json

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from fastapi.responses import Response, RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from db.requests import add_link, get_link_by_shortcode, search_link_by_url
from services.encoding import encoding_base52, decoding_base52


links_router = APIRouter(route_class=DishkaRoute)


@links_router.get("/{code}")
async def redirect(code: str, session: FromDishka[AsyncSession]):
    id = decoding_base52(code)
    link_field = await get_link_by_shortcode(session, id)

    if link_field:
        return RedirectResponse(link_field.original_url, 302)
    else:
        return Response(status_code=404)


@links_router.post("/create")
async def create_link(url: str, session: FromDishka[AsyncSession]):
    double_link = await search_link_by_url(session, url)
    if double_link:
        code = encoding_base52(double_link.id)
    else:
        link_field = await add_link(session, url)
        code = encoding_base52(link_field.id)
    return Response(status_code=200, content=json.dumps({"short_id": code, "target": url}))
