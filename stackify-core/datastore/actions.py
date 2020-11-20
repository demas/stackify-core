from pypika import Column
from pypika import Query
from pypika import Table

from datastore.repository import _execute
from models.questions import Question


def create_table():
    stmt = Query \
        .create_table("questions") \
        .columns(
            Column("question_id", "INTEGER"),
            Column("link", "VARCHAR"),
            Column("title", "VARCHAR"),
            Column("creation_date", "INTEGER"),
            Column("last_activity_date", "INTEGER"),
            Column("score", "INTEGER"),
            Column("answer_count", "INTEGER"),
            Column("view_count", "INTEGER"),
            Column("is_answered", "INTEGER"),
            Column("tags", "VARCHAR"),
            Column("category", "VARCHAR"),
            Column("subcategory", "VARCHAR"),
            Column("owner_reputation", "INTEGER")) \
        .primary_key("question_id")
    _execute(str(stmt))


def add_question(question: Question):
    questions = Table('questions')
    query = Query.into(questions).insert(*question.to_postgresql())
    _execute(str(query), question.to_postgresql())
