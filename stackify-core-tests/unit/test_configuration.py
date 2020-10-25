from configuration.config import StackifyConfig


def test_configuration_with_default_values():
    cfg = StackifyConfig()

    assert cfg.db_host == "localhost"
    assert cfg.db_name == "stackify"
    assert cfg.db_user == "stackify"
    assert cfg.db_password == "passw0rd"
    assert cfg.db_port == 5432


def test_configuration_with_custom_values():
    cfg = StackifyConfig(db_host="aws", db_name="db", db_user="user", db_password="qwerty", db_port=5431)

    assert cfg.db_host == "aws"
    assert cfg.db_name == "db"
    assert cfg.db_user == "user"
    assert cfg.db_password == "qwerty"
    assert cfg.db_port == 5431
