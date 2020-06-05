# _*_ coding:utf-8 _*_
import psutil,datetime
import platform
from pprint import pprint

class Monitor(object):
    def bytes_to_gb(self,data,key=''):
        if key == 'percent':
            return data
        return round(data / (1024**3),2)

    # 获取IP
    def getIp(self):
        addrs = psutil.net_if_addrs()
        addrs_info = {
            k: [
                val.address
                for val in v if val.family.name == 'AF_INET' and not val.address == '127.0.0.1'
            ]
            for k, v in addrs.items()
        }
        return addrs_info

    # 获取cpu信息
    def cpu(self):
        # percpu:True获取每个cpu的使用率 False获取平均使用率
        # 1.平均  2.单独 3.物理CPU核心数  4.逻辑CPU核心数
        data = dict(
            percent_avg = psutil.cpu_percent(interval=0,percpu=False),
            percent_per=psutil.cpu_percent(interval=0, percpu=True),
            num_p = psutil.cpu_count(logical=False),
            num_l=psutil.cpu_count(logical=True),
        )
        return data

    # 内存信息
    def mem(self):
        info = psutil.virtual_memory()
        data = dict(
            total=self.bytes_to_gb(info.total),
            used =self.bytes_to_gb(info.used),
            free = self.bytes_to_gb(info.free),
            percent = info.percent
        )
        return data

    # 交换分区
    def swap(self):
        info = psutil.swap_memory()
        data = dict(
            total=self.bytes_to_gb(info.total),
            used=self.bytes_to_gb(info.used),
            free=self.bytes_to_gb(info.free),
            percent=info.percent
        )
        return data

    def system(self):
        info = {
            'os_platform':platform.system(),
            'os_version':platform.platform(),
            'hostname':platform.node(),
        }

        return info

    # 磁盘信息
    def disk(self):
        info = psutil.disk_partitions()
        # 列表推导式
        data = {
            v.device:dict(
                device=v.device,
                mountpoint=v.mountpoint,
                fstype=v.fstype,
                opts = v.opts,
                used={
                    k:self.bytes_to_gb(v,k)
                    for k,v in psutil.disk_usage(v.mountpoint)._asdict().items()
                }
            )
            for v in info if v.fstype != ''
        }
        return data

    # 网络信息
    def net(self):
        addrs = psutil.net_if_addrs()
        addrs_info = {
            k:[
                dict(
                    family = val.family.name,
                    address = val.address,
                    netmask = val.netmask,
                    broadcast = val.broadcast
                )
                for val in v if val.family.name == 'AF_INET'
            ][0]
            for k,v in addrs.items()
        }
        io = psutil.net_io_counters(pernic=True)
        status = psutil.net_if_stats()
        data ={
            addrs_info[k]['address']:dict(
                name=k,
                bytes_sent=v.bytes_sent,
                bytes_recv = v.bytes_recv,
                packets_sent = v.packets_sent,
                packets_recv = v.packets_recv,
                **addrs_info[k]
            )
            for k,v in io.items() if status[k].isup == True
        }
        return data

    # 时间戳转换时间格式
    def td(self,tm):
        dt = datetime.datetime.fromtimestamp(tm)
        return dt.strftime('%Y-%m-%d %H:%M:%S')

    # 获取系统开机时间
    def last_start_time(self):
        return self.td(psutil.boot_time())

    # 获取系统登录用户
    def login_users(self):
        users = psutil.users()
        data = [
            dict(
                name=v.name,
                terminal=v.terminal,
                host=v.host,
                started=self.td(v.started),
                pid=v.pid
            )
            for v in users
        ]
        return data


if __name__ == '__main__':

    m = Monitor()
    '''
    for v in range(1,11):
        print(m.cpu())
        time.sleep(1)
    '''
    # pprint(m.net())

    print(psutil.net_io_counters(pernic=True))

    netsatus = psutil.net_if_stats()
    for k,v in netsatus.items():
        if v.isup == True:
            print(k)


