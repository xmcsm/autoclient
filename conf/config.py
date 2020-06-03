# 个性化配置文件
import os

BASEDIR = os.path.dirname(os.path.dirname(__file__))

MODE='agent'

CLIENTIP='192.168.56.1'

DEBUG = False

PLUGINS_DICT = {
    #'Basic':'src.plugins.basicinfo.Basic',
    'Disk':'src.plugins.diskinfo.Disk',
    'Cpu':'src.plugins.cpuinfo.Cpu',
    'Mem':'src.plugins.meminfo.Mem',
    'Net':'src.plugins.netinfo.Net',
    'Hardware':'src.plugins.hardware.Hardware',
}