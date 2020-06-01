from conf import config
from lib.conf import global_settings

class Setting():
    def __init__(self):

        for k in dir(global_settings):
            if k.isupper():
                setattr(self,k,getattr(global_settings,k))

        for k in dir(config):
            if k.isupper():
                setattr(self,k,getattr(config,k))

setting = Setting()