# 收集硬盘信息
from lib.monitor import Monitor

class Disk():
    def process(self,command,debug):
        # 处理磁盘信息
        output = Monitor().disk()
        return output