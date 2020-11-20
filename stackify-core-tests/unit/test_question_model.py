import pytest

from models.questions import Question


@pytest.mark.parametrize("is_answered", [True, False])
def test_question_model(is_answered):
    question = Question.new(
        link="one",
        title="title",
        is_answered=is_answered,
    )

    question_id, link, title, creation_date, \
        last_activity_data, score, answer_count, view_count, answered, \
        tags, category, subcategory, owner_reputation = question.to_postgresql()

    assert link == question.link
    assert title == question.title
    assert answered == (1 if is_answered else 0)
    assert category == "general"
    assert not subcategory
    assert owner_reputation == 0

