from create_bot import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from db_handlers.models import Post
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select

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




async def get_post() -> Post | None:
    async with AsyncSessionLocal() as session:
        try:
            result = await session.execute(
                select(Post).filter(Post.status == 'pending')
            )
            post = result.scalars().first()
            return post
        except SQLAlchemyError as e:
            print(f"Error loading post: {e}")
            return None