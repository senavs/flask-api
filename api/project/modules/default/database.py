from typing import Union

from flask import Blueprint, Flask

from .bases import FlaskBaseExtension
from ...database import DeclarativeBase, engine
from ...settings import database_env


class Database(FlaskBaseExtension):

    def init_app(self, app: Union[Flask, Blueprint]):
        super().init_app(app)

        if database_env.DATABASE_RESET:
            DeclarativeBase.metadata.drop_all(engine)
        DeclarativeBase.metadata.create_all(engine)
