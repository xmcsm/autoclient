import os
from lib.conf.conf import setting
from .boardinfo import Board
from .basicinfo import Basic

class Hardware:
    def process(self, command, debug):
        result = {}

        # basic = Monitor().system()
        basic = Basic().process(command,debug)
        result['basic'] = basic
        if basic['os_platform'] == 'linux':

            result['board'] = Board().process(command,debug)

            if debug:
                output = open(os.path.join(setting.BASEDIR, 'files/cpu.out'), 'r', encoding='utf8').read()
            else:
                output = command('cat /proc/cpuinfo')
            result['cpu'] = self.parseCpu(output)


        # 处理磁盘信息
        return result


    def parseCpu(self,content):
        result = {
            'cpu_count':0,
            'cpu_physical_count':0,
            'cpu_model':'',
        }
        cpu_physical_set = set()
        content = content.strip()
        for item in content.split('\n\n'):
            for row_line in item.split('\n'):
                key,value = row_line.split(':')
                key = key.strip()
                if key == 'processor':
                    result['cpu_count'] += 1
                elif key == 'physical id':
                    cpu_physical_set.add(value)
                elif key == 'model name':
                    if not result['cpu_model']:
                        result['cpu_model'] = value
        result['cpu_physical_count'] = len(cpu_physical_set)

        return result