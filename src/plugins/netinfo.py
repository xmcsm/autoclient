# 收集网络信息
from lib.monitor import Monitor

class Net():
    def process(self,command,debug):
        # 处理磁盘信息
        output = Monitor().net()
        return output