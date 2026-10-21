from sqlalchemy import func

from translate.extensions import db
from .base_model import BaseModel


class FlashCard(BaseModel):
    question = db.Column("question", db.String(100), unique=True)
    choice_1 = db.Column("choice_1", db.String(100))
    choice_2 = db.Column("choice_2", db.String(100))
    choice_3 = db.Column("choice_3", db.String(100))
    choice_4 = db.Column("choice_4", db.String(100))
    correct_choice = db.Column("correct_choice", db.String(100))

    def __init__(self, question, choice_1, choice_2, choice_3, choice_4, correct_choice):
        self.question = question
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        self.choice_3 = choice_3
        self.choice_4 = choice_4
        self.correct_choice = correct_choice

    def serialize(self):
        self_dict = {
            'id': str(self.id),
            'question' : str(self.question),
            'choices': {
                '1': str(self.choice_1),
                '2': str(self.choice_2),
                '3': str(self.choice_3),
                '4': str(self.choice_4)
            },
            'correct_choice': str(self.correct_choice)
        }
        return self_dict