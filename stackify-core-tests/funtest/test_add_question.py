from datastore.actions import add_question
from datastore.actions import create_table
from models.questions import Question
import os


def test_add_question():
    os.environ["stackify_db_name"] = "stackify_tests"
    create_table()
    q = Question.new(
        question_id=1,
        title="hello",
    )
    add_question(q)
