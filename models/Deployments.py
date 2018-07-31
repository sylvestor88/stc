"""
__author__ = "Sylvestor George"
__version__ = "1.0"
__maintainer__ = "Sylvestor George"
__email__ = "sylvestor.george88@gmail.com"
"""
from models.Base import BaseModel, db


class Deployments(BaseModel, db.Model):
    """Model for Deployments table"""

    __tablename__ = 'deployments'

    id = db.Column(db.Integer, primary_key=True)
    sha = db.Column(db.String(120))
    date = db.Column(db.Integer)
    action = db.Column(db.String(30))
    engineer = db.Column(db.String(120))
