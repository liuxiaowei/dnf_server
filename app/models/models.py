import json
import string
import random
from datetime import datetime
import hashlib


from .base import Base, db


class TUser(Base):
    __tablename__ = 't_user'

    mac = db.Column(db.String(255))
    last_login = db.Column(db.DateTime)
    status = db.Column(db.SmallInteger)
    ip = db.Column(db.String(255))



