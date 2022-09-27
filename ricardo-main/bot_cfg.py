from tg_datastore import TGDataStore
from json import dumps


def write_config():
    global global_config
    datastore.write_field(datastore_field_id, global_config)


def read_config() -> dict:
    global global_config
    global_config = datastore.read_field(datastore_field_id)


tg_api_id = 10672866
tg_api_hash = "09d230d6d582fc7b8139036fd7374c0e"
tg_bot_token = "5472991102:AAH8xnan-C3KDXevlnKxIvWb6kFih4dLFmQ"
datastore_store_id = -1001742753765
datastore_field_id = 4
global_config = {}

datastore = TGDataStore(tg_bot_token, datastore_store_id)

read_config()
print("Config:\n", dumps(global_config, indent=4))
