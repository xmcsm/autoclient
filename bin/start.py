
from src.plugins import PluginsManager

import requests,json

if __name__ == '__main__':
    res = PluginsManager().execute()
    requests.post('http://127.0.0.1:8000/asset/', data=json.dumps(res))