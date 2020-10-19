from typing import List, Optional

from models.questions import Question


class Classifier:
    def __init__(self, stop_tags, first_level_rules):
        self.stop_tags = stop_tags
        self.first_level_rules = first_level_rules

    def _has_stop_tag(self, tags: List[str]) -> bool:
        for tag in tags:
            if tag in self.stop_tags:
                return True
        return False

    def _first_level_classification(self, tags: List[str], site: str) -> Optional[str]:
        for rule in self.first_level_rules:
            if rule["site"] == site and rule["include"] == "*":
                return rule["result"]
            elif rule["site"] == site:
                for rule_tag in rule["include"].split(","):
                    if rule_tag in tags:
                        return rule["result"]
        return "none"

    # TODO: add test for this method
    def classify(self, questions: List[Question]) -> List[Question]:
        def add_category(question: Question) -> Question:
            question.category = self._first_level_classification(question.tags, question.site)
            return question

        questions = filter(lambda q: not self._has_stop_tag(q.tags), questions)
        return list(map(add_category, questions))

