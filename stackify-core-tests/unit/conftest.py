import requests

import pytest

RAW_RESPONSE = """
    {"items":[{"tags":["memory","cpu","memory-alignment"],"owner":{"reputation":55,"user_id":12320997,
    "user_type":"registered",
    "profile_image":"https://lh6.googleusercontent.com/-WhasCfvwxBg/AAAAAAAAAAI/AAAAA/ACHiSv48g0w/photo.jpg?sz=128",
    "display_name":"Anton Tretyakov","link":"https://stackoverflow.com/users/12320997/anton-tretyakov"},
    "is_answered":false,"view_count":1,"answer_count":0,"score":0,"last_activity_date":1603034693,
    "creation_date":1603034693,"question_id":64415023,"content_license":"CC BY-SA 4.0",
    "link":"https://stackoverflow.com/questions/64415023/why-cpu-accesses-aligned-memory",
    "title":"Why CPU accesses aligned memory"},{"tags":["sqlalchemy","decimal"],
    "owner":{"reputation":3303,"user_id":6515755,"user_type":"registered",
    "profile_image":"https://graph.facebook.com/1064376696971764/picture?type=large","display_name":"Ryabchenko Alexander",
    "link":"https://stackoverflow.com/users/6515755/ryabchenko-alexander"},"is_answered":false,"view_count":5,
    "answer_count":0,"score":0,"last_activity_date":1603034691,"creation_date":1603034060,"last_edit_date":1603034691,
    "question_id":64414922,"content_license":"CC BY-SA 4.0",
    "link":"https://stackoverflow.com/questions/64414922/save-decimal-with-sqlalchemy",
    "title":"Save Decimal with SQLAlchemy"}],"has_more":false,"quota_max":300,"quota_remaining":241}
"""


@pytest.fixture
def patched_good_request(monkeypatch):
    def mocked_get(url, *args, **kwargs):
        mock = type('MockedReq', (), {})()
        mock.text = RAW_RESPONSE
        mock.status_code = 200
        return mock
    monkeypatch.setattr(requests, 'get', mocked_get)


@pytest.fixture
def patched_bad_request(monkeypatch):
    def mocked_get(url, *args, **kwargs):
        mock = type('MockedReq', (), {})()
        mock.status_code = 500
        return mock
    monkeypatch.setattr(requests, 'get', mocked_get)
