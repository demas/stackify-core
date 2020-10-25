from betterconf import field
from betterconf import Config
from betterconf.caster import to_int

# TODO: implement provider to load values from config file
# https://github.com/fscdev/betterconf


class StackifyConfig(Config):
    db_host = field("stackify_db_host", default="localhost")
    db_name = field("stackify_db_name", default="stackify")
    db_user = field("stackify_db_user", default="stackify")
    db_password = field("stackify_db_password", default="passw0rd")
    db_port = field("stackify_db_port", default=5432, caster=to_int)
