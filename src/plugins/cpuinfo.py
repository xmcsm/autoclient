# 收集CPU信息
from lib.monitor import Monitor
import subprocess

class Cpu():
    def process(self,command,debug):
        # 处理磁盘信息
        monitor = Monitor()
        cpuinfo = monitor.cpu()

        return cpuinfo