from pydantic import BaseModel


class UserBase(BaseModel):
    email: str

    class ConfigDict:
        from_attributes = True


class UserCreate(UserBase):
    password: str


class UserGet(UserBase):
    id: int
