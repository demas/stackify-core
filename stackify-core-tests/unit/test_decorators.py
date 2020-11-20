from unittest.mock import Mock

from datastore.decorator import with_connection


def test_with_connection():
    mock = Mock()
    with_connection(mock)()
    mock.assert_called_once()

