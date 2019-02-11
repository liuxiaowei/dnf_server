import json
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from app.libs.error import HTTPError


__all__ = ['db', 'Base']


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def save(self, auto_update=True):
        if auto_update and hasattr(self, 'updated_at'):
            self.updated_at = datetime.now()

        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def reload(self):
        db.session.refresh(self)

    def to_json(self, col):
        if not col:
            return None

        return json.loads(col)

    def format_datetime(self, col):
        if not isinstance(col, datetime):
            return col

        if col is None:
            return 0

        return int(col.timestamp())

    def remaining_seconds(self, col):
        if not isinstance(col, datetime):
            return 0

        if col is None:
            return 0

        dt_now = datetime.now()
        if col > dt_now:
            return (col - dt_now).seconds

        return 0


    @classmethod
    def get_by_id(cls, id):
        res = cls.query.get(id)
        if res is None:
            raise HTTPError(1, '无数据, table: {}, id: {}'.format(cls.__tablename__, id))
        return res

    @classmethod
    def get_by_userid(cls, userid):
        res = cls.query.filter_by(userid=userid).first()
        if res is None:
            raise HTTPError(1, '无数据, table: {}, userid: {}'.format(cls.__tablename__, userid))
        return res

    def to_dict(self):
        res = {}
        for key in self.__dict__:
            if key.startswith('_'):
                continue

            if isinstance(self.__dict__[key], datetime):
                res[key] = int(self.__dict__[key].timestamp())
            else:
                res[key] = self.__dict__[key]
        return res