from create_bot import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from db_handlers.models import Post
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import func

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

async def delete_post(post_id: int) -> bool:
    async with AsyncSessionLocal() as session:
        try:
            post = await session.get(Post, post_id)
            if post is not None:
                await session.delete(post)
                await session.commit()
                return True
            return False

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


async def count_posts() -> int:
    async with AsyncSessionLocal() as session:
        try:
            result = await session.execute(
                select(func.count(Post.id))
            )
            count = result.scalar()
            return count
        except SQLAlchemyError as e:
            print(f"Error loading posts: {e}")
            return 0