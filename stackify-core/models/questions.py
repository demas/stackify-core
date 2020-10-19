from schematics.models import Model
from schematics.types import BooleanType, IntType, StringType, TimestampType, URLType


class Question(Model):
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
