import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import logging.config
from src.plugins import PluginsManager
from lib.conf.conf import setting
from time import sleep
import requests,json
logging.config.dictConfig(setting.LOGGING_DIC)
from pprint import pprint



if __name__ == '__main__':
    logger=logging.getLogger('接口调用')
    while True:
        res = PluginsManager().execute()
        logger.info(res)
        response = requests.post('http://{0}:{1}/asset/'.format(setting.SERVER_IP,setting.SERVER_PORT), data=json.dumps(res))
        logger.info(response.status_code)
        sleep(setting.AUTO_SECOND)