from sqlalchemy import func

from translate.extensions import db
from .base_model import BaseModel


class User(BaseModel):
    email = db.Column("email", db.String(100))
    user_name = db.Column("user_name", db.String(100), unique=True)
    score = db.Column("score", db.Integer, nullable=True, default=0)

    def __init__(self, email, user_name):
        self.email = email
        self.user_name = user_name

    def serialize(self):
        self_dict = {
            'id': str(self.id),
            'user_name': str(self.user_name if self.user_name else ""),
            'email': str(self.email),
            'score': str(self.score)
        }
        return self_dict