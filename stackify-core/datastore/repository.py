from typing import List

from datastore.decorator import with_connection


@with_connection
def _execute(query: str, params=tuple(), conn=None):
    with conn.cursor() as cur:
        cur.execute(query, params)


def _select(query: str, conn=None) -> List:
    with conn.cursor() as cur:
        cur.execute(query)
        result = cur.fecthall()
    return result
