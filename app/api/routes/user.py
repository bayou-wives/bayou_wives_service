from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.models.user import UserGet, UserCreate
from app.db.session import SessionLocal, get_db_session
from app.db.models.User import User
from app.services.user_service import UserService

router = APIRouter()


@router.post('/users')
def create_user(user: UserCreate, db_session: SessionLocal = Depends(get_db_session)):
    user_service = UserService(db_session=db_session)
    existing_user: User = user_service.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail=f'User account with email {user.email} already exists'
        )

    return user_service.create_user(user)


@router.get('/users', response_model=List[UserGet])
def get_users(db_session: SessionLocal = Depends(get_db_session)):
    user_service = UserService(db_session=db_session)
    all_users = user_service.get_all_users()
    if not all_users:
        return HTTPException(
            status_code=404,
            detail='No users found'
        )
    return all_users


@router.get('/users/{user_id}', response_model=UserGet)
def get_user_by_id(user_id: int, db_session: SessionLocal = Depends(get_db_session)):
    user_service = UserService(db_session=db_session)
    user = user_service.get_user_by_id(user_id)
    if not user:
        return HTTPException(
            status_code=404,
            detail='User not found'
        )
    return user
