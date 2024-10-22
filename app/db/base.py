"""
Import all the models so that Base has them before being imported by Alembic
"""
from .models.Base import Base
from .models.User import User
