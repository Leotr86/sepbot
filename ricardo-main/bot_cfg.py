from tg_datastore import TGDataStore
from json import dumps


def write_config():
    global global_config
    datastore.write_field(datastore_field_id, global_config)


def read_config() -> dict:
    global global_config
    global_config = datastore.read_field(datastore_field_id)


tg_api_id = 14681595
tg_api_hash = "a86730aab5c59953c424abb4396d32d5"
tg_bot_token = "5356126817:AAFfdxFDSQRvANKvjnWNoBGCxY0sZAefVcA"
datastore_store_id = -1001695628050
datastore_field_id = 4
global_config = {}

datastore = TGDataStore(tg_bot_token, datastore_store_id)

read_config()
print("Config:\n", dumps(global_config, indent=4))
