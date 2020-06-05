from lib.conf.conf import setting
import importlib
import subprocess,paramiko
import traceback

class PluginsManager():
    def __init__(self):
        self.plugins_dict = setting.PLUGINS_DICT
        self.mode = setting.MODE
        self.Debug = setting.DEBUG

    def execute(self):
        response = {}
        response['CLIENTIP'] = setting.CLIENT_IP
        for k,v in self.plugins_dict.items():
            ret = {'status':None,'data':None}
            try:
                module_path,class_name = v.rsplit('.',1)
                m= importlib.import_module(module_path)
                cls = getattr(m,class_name)
                res = cls().process(self.command,self.Debug)
                ret['status'] = 10000
                ret['data'] = res
            except Exception as e:
                ret['status'] = 10001
                ret['data'] = {'message':str(traceback.format_exc())}
            response[k] = ret
        return response

    def command(self,cmd):

        if self.mode == 'agent':
            res = subprocess.getoutput(cmd)
            ip = res
            return ip
        elif self.mode == 'ssh':
            ssh = paramiko.SSHClient()

            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname='192.168.56.1',port=10022,username='root',password='getstart')

            stdin,stdout,stderr = ssh.exec_command(cmd)
            res = stdout.read()
            ssh.close()
            return res
        elif self.mode == 'salt':
            pass
        else:
            raise Exception('只支持agent/ssh/salt模式')