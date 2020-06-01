# 收集主板信息
from lib.monitor import Monitor


class Basic():
    def process(self,command,debug):
        # 处理磁盘信息
        if debug:
            output = {
                'os_platform':'linux',
                'os_version':'CentOS release 7.7',
                'hostname':'python'
            }
        else:
            output = Monitor().system()

        return output