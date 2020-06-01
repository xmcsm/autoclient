import os
from lib.conf.conf import setting
class Board():
    def process(self,command,debug):
        # 处理磁盘信息
        if debug:
            output = open(os.path.join(setting.BASEDIR,'files/board.out'),'r',encoding='utf8').read()
        else:
            output = command('dmidecode -t1')

        return self.parse(output)

    def parse(self,content):
        result = {}
        key_map = {
            'Manufacturer':'Manufacturer',
            'Product Name':'Product Name',
            'Serial Number':'Serial Number',
        }

        for item in content.split('\n'):
            row_data = item.strip().split(':')

            if len(row_data) == 2:
                if row_data[0] in key_map:
                    result[key_map[row_data[0]]] = row_data[1].strip() if row_data[1] else row_data[1]
        return result