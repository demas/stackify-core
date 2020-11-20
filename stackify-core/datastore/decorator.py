import psycopg2

from configuration.config import StackifyConfig


def _connection(config: StackifyConfig):
    conn = psycopg2.connect(
        database=config.db_name,
        user=config.db_user,
        password=config.db_password,
        host=config.db_host,
        port=config.db_port
    )
    return conn


def with_connection(f, auto_commit=True):
    def wrapped(*args, **kwargs):
        connection = kwargs.get("conn", None)

        if not connection:
            config = StackifyConfig()
            connection = _connection(config)
            kwargs["conn"] = connection
        result = f(*args, **kwargs)

        if auto_commit:
            connection.commit()

        return result
    return wrapped
