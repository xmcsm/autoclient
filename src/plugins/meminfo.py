# 收集内存信息
from lib.monitor import Monitor

class Mem():
    def process(self,command,debug):
        # 处理磁盘信息
        output = Monitor().mem()
        return output