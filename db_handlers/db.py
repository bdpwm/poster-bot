from create_bot import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from db_handlers.models import Post
from sqlalchemy.exc import SQLAlchemyError

async def save_post(user_id: int, content: str, photo_path: str = None) -> bool:
    async with AsyncSessionLocal() as session:
        try:
            post = Post(user_id=user_id, content=content, photo_path=photo_path)
            session.add(post)
            await session.commit()
            return True

        except SQLAlchemyError as e:
            await session.rollback()
            return False