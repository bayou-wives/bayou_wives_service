from sqlalchemy.orm import Session

from .security_service import SecurityService
from ..db.models.User import User
from ..models.user import UserCreate, UserGet


class UserService:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.security_service = SecurityService()

    def create_user(self, user: UserCreate):
        hashed_password = self.security_service.get_password_hash(user.password)
        new_user = User(
            email=user.email,
            hashed_password=hashed_password
        )
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)
        return new_user

    def get_all_users(self):
        return self.db_session.query(User).all()

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.db_session.get(User, user_id)

    def get_user_by_email(self, email: str) -> User | None:
        return self.db_session.query(User).where(
            User.email == email
        ).scalar()
