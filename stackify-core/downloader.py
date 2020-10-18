import json
import time
from typing import List
from typing import NamedTuple
from typing import Tuple

import requests

from exceptions import DownloadQuestionsError
from model import Question

# TODO: formatted string
URL_TEMPLATE = "https://api.stackexchange.com/2.2/questions?pagesize=100&page={}&fromdate={}&order=desc&sort=creation&site={}&key={}"

# TODO: move to config (?)
KEY = ""
SITES = ["stackoverflow", "codereview", "askdifferent"]


class Result(NamedTuple):
    questions: List
    last_sync: int
    quota_remain: int


def _make_url(from_time: int, site: str, key: str):
    return lambda page: URL_TEMPLATE.format(page, from_time, site, key)


def _convert_question(question: dict, site: str) -> Question:
    question["site"] = site
    question["tags"] = ",".join(question["tags"])
    question["owner_reputation"] = question["owner"]["reputation"]
    return Question(question, strict=False)


def _fetch_one_site(site: str, from_time: int) -> Tuple[List[Question], int]:
    url_template = _make_url(from_time, site, KEY)
    page = 1
    result = []

    while True:
        response = requests.get(url=url_template(page))
        if response.status_code != 200:
            raise DownloadQuestionsError(status_code = response.status_code)

        json_data = json.loads(response.text)
        result += [_convert_question(question, site) for question in json_data["items"]]
        page = page + 1
        if not json_data['has_more']:
            break

    return result, json_data["quota_remaining"]


def fetch(from_time: int, sites: List[str] = None) -> Result:
    sites = sites if sites else SITES
    current_moment = int(time.time()) # TODO: use arrow instead?
    quota = 0
    result = []

    for site in sites:
        questions, quota = _fetch_one_site(site=site, from_time=from_time)
        result = result + questions

    return Result(questions=result, last_sync=current_moment, quota_remain=quota)
