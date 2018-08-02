"""
__author__ = "Sylvestor George"
__version__ = "1.0"
__maintainer__ = "Sylvestor George"
__email__ = "sylvestor.george88@gmail.com"
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Gets current path of the directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# DB Engine
engine = create_engine(
    'sqlite:///{0}/deploys.sqlite'.format(current_dir, convert_unicode=True))

# DB Session
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
