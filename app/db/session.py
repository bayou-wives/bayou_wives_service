from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..core.config import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI.unicode_string(),
    pool_pre_ping=True,
    echo=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session():
    db_session = SessionLocal()
    try:
        yield db_session
    except Exception as e:
        raise e
    finally:
        db_session.close()
