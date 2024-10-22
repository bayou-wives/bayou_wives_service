import os
from passlib.context import CryptContext


class SecurityService:
    def __init__(self):
        self.secret_key = os.getenv('HASHING_SECRET_KEY')
        self.hashing_algorithm = os.getenv('HASHING_ALGORITHM')
        self.crypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.crypt_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str):
        return self.crypt_context.hash(password)
