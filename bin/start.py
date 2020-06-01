from lib.conf.conf import setting
from lib.monitor import Monitor
from src.plugins import PluginsManager
from pprint import pprint
import requests,json

if __name__ == '__main__':
    res = PluginsManager().execute()
    pprint(res)
        # requests.post('http://127.0.0.1:8000/asset/', data=json.dumps(res))