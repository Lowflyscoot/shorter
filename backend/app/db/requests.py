
from app.db.models import links
from app.services.tools import get_random_string
from sqlalchemy import select


async def add_link(db, user_url: str) -> links.Link:
    link = links.Link(original_url=user_url)

    db.add(link)
    await db.commit()
    await db.refresh(link)

    return link

async def get_link_by_shortcode(db, id: int):
    result =  await db.execute(
        select(links.Link).where(links.Link.id == id)
    )
    return result.scalar_one_or_none()

async def search_link_by_url(db, url: str):
    result =  await db.execute(
        select(links.Link).where(links.Link.original_url == url)
    )
    return result.scalars().first()

