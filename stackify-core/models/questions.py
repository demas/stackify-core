from schematics.types import BooleanType
from schematics.types import IntType
from schematics.types import StringType
from schematics.types import TimestampType
from schematics.types import URLType

from common.models import BaseModel


class Question(BaseModel):
    question_id = IntType(required=True)
    link = URLType(required=True)
    title = StringType(required=True)
    creation_date = TimestampType(required=True)
    last_activity_date = TimestampType(required=True)
    score = IntType(required=True, default=0)
    answer_count = IntType(required=True, default=0)
    view_count = IntType(required=True, default=0)
    is_answered = BooleanType(required=True, default=False)
    tags = StringType(required=True)
    site = StringType(required=True)
    category = StringType(required=True, default="general")
    subcategory = StringType()
    owner_reputation = IntType(required=True, default=0)

    def to_postgresql(self):
        return (
            self.question_id,
            self.link,
            self.title,
            self.creation_date,
            self.last_activity_date,
            self.score,
            self.answer_count,
            self.view_count,
            1 if self.is_answered else 0,
            self.tags,
            self.category,
            self.subcategory,
            self.owner_reputation,
        )
