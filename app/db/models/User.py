from sqlalchemy.types import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from .Base import Base


class User(Base):
    email: Mapped[str] = mapped_column(String(50))
    hashed_password: Mapped[str] = mapped_column(String(100))
