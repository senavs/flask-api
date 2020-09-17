from typing import Optional, Union, List

from werkzeug.exceptions import NotFound
from sqlalchemy.orm.query import Query

from .. import DeclarativeBase
from .connector import Connector


class BaseModel:

    @classmethod
    def find_one(cls, connection: Connector, identifier: int, *, raise_not_found: bool = False) -> DeclarativeBase:
        result = connection.query(cls).get(identifier)
        if raise_not_found and not result:
            raise NotFound('identifier not found')
        return result

    @classmethod
    def find_filter(cls, connection: Connector, **kwargs) -> Query:
        result = connection.query(cls).filter_by(**kwargs)
        return result

    @classmethod
    def find_all(cls, connection: Connector, *, as_query: bool = False) -> Union[Query, List[DeclarativeBase]]:
        result = connection.query(cls)
        return result if as_query else result.all()

    def add(self, connection: Connector, *, commit: bool = True):
        connection.session.add(self)
        if commit:
            connection.commit()

    def delete(self, connection: Connector, *, commit: bool = True):
        connection.session.delete(self)
        if commit:
            connection.commit()

    def to_dict(self, *, exclude: Optional[list] = None, **include) -> dict:
        if not exclude:
            exclude = []

        attrs = {attr.lower(): getattr(self, attr) for attr in self.__dir__() if attr.isupper() and attr not in exclude}
        attrs.update(**include)
        return attrs

    def __repr__(self):
        return f'{type(self).__qualname__}({self.to_dict()})'
