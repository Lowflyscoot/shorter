from sqlalchemy import select

from .models import links


async def add_link(session, user_url: str) -> links.Link:
    link = links.Link(original_url=user_url)

    async with session() as db:
        db.add(link)
        await db.commit()
        await db.refresh(link)

    return link


async def get_link_by_shortcode(session, id: int):
    async with session() as db:
        result =  await db.execute(
            select(links.Link).where(links.Link.id == id)
        )
    return result.scalar_one_or_none()


async def search_link_by_url(session, url: str):
    async with session() as db:
        result =  await db.execute(
            select(links.Link).where(links.Link.original_url == url)
        )
    return result.scalars().first()
