from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy_utils import UUIDType, PasswordType
import uuid


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(UUIDType, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(PasswordType(schemes=["pbkdf2_sha512"]))
    access_token = Column(UUIDType)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.id = uuid.uuid4()
        self.access_token = uuid.uuid4()

    def recreate_access_token(self):
        self.access_token = uuid.uuid4()

    def __repr__(self):
        return "<User(%s)>" % self.username


class System(Base):
    __tablename__ = 'systems'

    id = Column(UUIDType, primary_key=True)
    username = Column(String)
    email = Column(String)
    access_token = Column(UUIDType)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.id = uuid.uuid4()
        self.access_token = uuid.uuid4()

    def recreate_access_token(self):
        self.access_token = uuid.uuid4()

    def __repr__(self):
        return "<User(%s)>" % self.username
