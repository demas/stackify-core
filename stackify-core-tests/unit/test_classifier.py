from classifier.classifier import Classifier

STOP_TAGS = ["stop_a", "stop_b", "stop_c"]

FIRST_LEVEL_RULES = [
    {"site": "site_a", "include": "a",      "result": "result_1"},
    {"site": "site_a", "include": "b",      "result": "result_2"},
    {"site": "site_a", "include": "c",      "result": "result_2"},
    {"site": "site_a", "include": "d,e,f",  "result": "result_3"},
    {"site": "site_b", "include": "x",      "result": "result_4"},
    {"site": "site_b", "include": "y,z",    "result": "result_6"},
    {"site": "site_b", "include": "a",      "result": "result_7"},
    {"site": "site_b", "include": "*",      "result": "result_5"},
    {"site": "site_c", "include": "x",      "result": "result_8"},
    {"site": "site_c", "include": "z",      "result": "result_9"},
]

classifier = Classifier(STOP_TAGS, FIRST_LEVEL_RULES)


def test_stop_tag_stop_present():
    assert classifier._has_stop_tag(["cassandra", "stop_a", "oracle"])
    assert classifier._has_stop_tag(["stop_b", "stop_a", "oracle"])


def test_stop_tag_stop_not_present():
    assert not classifier._has_stop_tag(["cassandra", "java", "oracle"])


def test_first_level_classifier_found():
    assert classifier._first_level_classification(["some", "another", "a"], "site_a") == "result_1"
    assert classifier._first_level_classification(["a", "some", "another"], "site_a") == "result_1"
    assert classifier._first_level_classification(["c", "some", "another"], "site_a") == "result_2"


def test_first_level_classifier_not_found():
    assert classifier._first_level_classification(["some", "another", "here"], "site_a") == "none"


def test_first_level_classifier_multiple_sites_one_unique_tag():
    assert classifier._first_level_classification(["some", "x", "here"], "site_b") == "result_4"
    assert classifier._first_level_classification(["some", "x", "here"], "site_c") == "result_8"


def test_first_level_classifier_multiple_sites_many_tags():
    assert classifier._first_level_classification(["some", "z", "here"], "site_b") == "result_6"


def test_first_level_classifier_multiple_sites_not_unique_site():
    assert classifier._first_level_classification(["some", "a", "here"], "site_b") == "result_7"
    assert classifier._first_level_classification(["some", "a", "here"], "site_a") == "result_1"


def test_first_level_classifier_missing_tags_and_star_condition():
    assert classifier._first_level_classification(["some", "where", "here"], "site_b") == "result_5"


def test_first_level_classifier_found_combined():
    assert classifier._first_level_classification(["some", "another", "f"], "site_a") == "result_3"


def test_first_level_classifier_not_existing_site():
    assert classifier._first_level_classification(["some", "another", "a"], "site_x") == "none"


def test_first_level_classifier_empty_tags():
    assert classifier._first_level_classification([], "site_x") == "none"


def test_first_level_classifier_duplicate_tags():
    assert classifier._first_level_classification(["a", "a", "a"], "site_a") == "result_1"

