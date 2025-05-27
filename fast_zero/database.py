from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

engine = create_async_engine('sqlite+aiosqlite:///database.db')
# Cria a engine de conexão assíncrona com o banco de dados


async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as session:
        # `AsyncSession` gerencia a sessão assíncrona com o banco de dados
        # `expire_on_commit=False` evita que os objetos sejam expirados após o commit,
        # O comportamento padrão do SQLAlchemy é expirar o chace dos objetos após o commit.
        yield session
