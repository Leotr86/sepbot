from tg_datastore import TGDataStore
from json import dumps


def write_config():
    global global_config
    datastore.write_field(datastore_field_id, global_config)


def read_config() -> dict:
    global global_config
    global_config = datastore.read_field(datastore_field_id)


tg_api_id = 12244448
tg_api_hash = "890bdfa19a5ce152a64a80917fe7be29"
tg_bot_token = "5478857996:AAGNVPRBE0VaOWqQD4CljEMf0tBUImDAjxA"
datastore_store_id = -1001695628050
datastore_field_id = 4
global_config = {}

datastore = TGDataStore(tg_bot_token, datastore_store_id)

read_config()
print("Config:\n", dumps(global_config, indent=4))
