from unittest import mock

import pytest

import downloader
from exceptions import DownloadQuestionsError


def test_make_url():
    url_producer = downloader._make_url(from_time=10, site="stackoverflow", key="secret_key")

    url = url_producer(1)
    assert url == "https://api.stackexchange.com/2.2/questions?pagesize=100&" + \
                  "page=1&fromdate=10&order=desc&sort=creation&site=stackoverflow&key=secret_key"

    url = url_producer(2)
    assert url == "https://api.stackexchange.com/2.2/questions?pagesize=100&" + \
                  "page=2&fromdate=10&order=desc&sort=creation&site=stackoverflow&key=secret_key"

    url = url_producer(10)
    assert url == "https://api.stackexchange.com/2.2/questions?pagesize=100&" + \
                  "page=10&fromdate=10&order=desc&sort=creation&site=stackoverflow&key=secret_key"


def test_download_ok(patched_good_request):
    with mock.patch("time.time", return_value=10):
        result = downloader.fetch(from_time=10, sites=["stackoverflow"])

    assert result.last_sync == 10
    assert result.quota_remain == 241
    assert len(result.questions) == 2
    assert all([q.tags for q in result.questions])
    assert all([q.owner_reputation for q in result.questions])
    assert all([q.site == "stackoverflow" for q in result.questions])


def test_download_not_ok(patched_bad_request):
    with pytest.raises(DownloadQuestionsError) as e:
        downloader.fetch(from_time=10, sites=["stackoverflow"])

    error_message = "Error downloading questions"
    assert e.value.message == error_message
