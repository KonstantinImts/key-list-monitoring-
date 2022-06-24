from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.exceptions import ValidationError
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt

from passlib.hash import bcrypt

from .. import tables
from ..database import Session, get_session
from ..models.auth import Token, User, UserCreate
from ..settings import settings


oath2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in')  # обявляем схему с формой авторизации


def get_current_user(token: str = Depends(oath2_scheme)) -> User:
    '''Get the current user.'''
    return AuthService.validate_token(token)


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        '''Checking the hash of the original string and the encrypted password.'''
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        '''Password hashing.'''
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> User:
        '''Token validation.'''
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError:
            raise HTTPException(status_code=406, detail='Could not validate credentials.') from None
        user_data = payload.get('user')
        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise HTTPException(status_code=406, detail='Could not validate credentials.') from None
        return user

    @classmethod
    def create_token(cls, user: tables.User) -> Token:
        '''Creation of a token.'''
        user_data = User.from_orm(user)  # преобразуем из модели orm в модел pydantic
        now = datetime.utcnow()
        payload = {
            'iat': now,  # время создания токена
            'nbf': now,  # время до которой токен нельзя использовать (в формате UTC!)
            'exp': now + timedelta(seconds=settings.jwt_expiration),  # время истечения токена
            'sub': str(user_data.id),  # обозначает пользователя которому выдан токен
            'user': user_data.dict(),  # модель пользователя в виде словаря
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )
        return Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int) -> tables.User:
        '''Protected feature. Get the user if it exists.'''
        user = (
            self.session
            .query(tables.User)
            .filter_by(id=user_id)
            .first()
        )
        if not user:
            raise HTTPException(status_code=406, detail='User with this id does not exist.') from None
        return user

    def _check_role_by_user_id(self, user_id: int, role_name: str) -> tables.User:
        '''Checking if a user is in a role.'''
        user = AuthService._get(self, user_id)
        if user.role_name == role_name:
            return user

    def register_new_user(self, user_data: UserCreate) -> Token:
        '''New User Registration. Registration also requires authorization.'''
        user = tables.User(
            email=user_data.email,
            username=user_data.username,
            password_hash=self.hash_password(user_data.password),
            sex=user_data.sex,
        )
        self.session.add(user)
        self.session.commit()
        return self.create_token(user)

    def authenticate_user(self, username: str, password: str) -> Token:
        '''Authentication.'''
        user = (
            self.session
            .query(tables.User)
            .filter(tables.User.username == username)
            .first()
        )
        if not User:
            raise HTTPException(status_code=406, detail='Incorrect username or password.') from None
        if not self.verify_password(password, user.password_hash):
            raise HTTPException(status_code=406, detail='Incorrect username or password.') from None
        return self.create_token(user)

    def get(self, user_id: int) -> tables.User:
        '''Get a specific user.'''
        return self._get(user_id)
