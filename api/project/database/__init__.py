from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from ..settings import database_env

engine = create_engine(database_env.DATABASE_URI, echo=False)
DeclarativeBase = declarative_base()
Session = sessionmaker(engine)
