import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.environ["DATABASE_URI"])

Session = scoped_session(sessionmaker(bind=engine))
session = Session()
