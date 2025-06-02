from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from fast_zero.settings import Settings


# engine = create_async_engine(Settings().DATABASE_URL) # type: ignore

engine = create_async_engine("postgresql+asyncpg://postgres:123456@localhost:5432/teste", echo=True)


async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session
