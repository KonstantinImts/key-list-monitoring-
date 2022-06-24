from typing import List

from fastapi import Depends

from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session


class UserService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.User]:
        '''Get a list of all users.'''
        query = self.session.query(tables.User)
        users = query.all()
        return users
