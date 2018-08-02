"""
__author__ = "Sylvestor George"
__version__ = "1.0"
__maintainer__ = "Sylvestor George"
__email__ = "sylvestor.george88@gmail.com"
"""
from sqlalchemy import Column, Integer, String, inspect
from db.sqlite import Base


class Deployments(Base):
    """Model for events table
    """

    __tablename__ = 'deploys'

    id = Column(Integer, primary_key=True)
    sha = Column(String(40))
    date = Column(Integer)
    action = Column(String(8))
    engineer = Column(String(32))

    def __init__(self, sha=None, date=None, action=None, engineer=action):
        self.sha = sha
        self.date = date
        self.action = action
        self.engineer = engineer

    def model_obj_as_dict(self):
        """
        Return a dictionary representation of this model
        """
        return {
            c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs
        }
