from environs import Env
import os

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
BOT_ADMINS = env.list("BOT_ADMINS", subcast=int)
THROTTLE_RATE = env.float("THROTTLE_RATE")

PSQL_HOSTNAME = env.str("PSQL_HOSTNAME")
PSQL_PORT = env.int("PSQL_PORT")
PSQL_USERNAME = env.str("PSQL_USERNAME")
PSQL_PASSWORD = env.str("PSQL_PASSWORD")
PSQL_DB_NAME = env.str("PSQL_DB_NAME")

DIRNAME = os.path.dirname(__file__)
os.chdir(f"{DIRNAME}//..")

one_model = dict(
    type='Первое'
)
two_model = dict(
    type='Второе'
)
three_model = dict(
    type='Третье'
)

MESSAGE_MODEL = dict(
    change_first=one_model,
    change_second=two_model,
    change_third=three_model
)
