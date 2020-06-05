# 个性化配置文件
import os

BASEDIR = os.path.dirname(os.path.dirname(__file__))

# 模式
MODE='agent'

# 客户端IP
CLIENT_IP = '192.168.56.1'

# 服务端IP
SERVER_IP = '192.168.56.1'

# 服务端端口
SERVER_PORT = '8000'

# 间隔X秒抽取指标
AUTO_SECOND = 60

# 调试模式
DEBUG = False

PLUGINS_DICT = {
    #'Basic':'src.plugins.basicinfo.Basic',
    'Disk':'src.plugins.diskinfo.Disk',
    'Cpu':'src.plugins.cpuinfo.Cpu',
    'Mem':'src.plugins.meminfo.Mem',
    'Net':'src.plugins.netinfo.Net',
    'Hardware':'src.plugins.hardware.Hardware',
    'Swap':'src.plugins.swap.Swap',
}

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

test_format = '%(asctime)s] %(message)s'

# default日志保存路径
DEFAULT_LOG_PATH = os.path.join(BASEDIR,'log', 'default.log')
# other日志保存路径
OTHER_LOG_PATH = os.path.join(BASEDIR,'log', 'other.log')

# 3、日志配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'test': {
            'format': test_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'formatter': 'standard',
            # 可以定制日志文件路径
            'filename': DEFAULT_LOG_PATH,  # 日志文件
            'maxBytes': 1024*1024*100,  # 日志大小 5M
            'backupCount': 10,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        'other': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'test',
            'filename': OTHER_LOG_PATH,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG', # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        '接口调用': {
            'handlers': ['default',],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG', # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        '专门的采集': {
            'handlers': ['other',],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}