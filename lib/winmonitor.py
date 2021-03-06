# -*- coding: utf-8 -*-
import os, sys
import wmi
c = wmi.WMI()

def getBoard():
    boards = {}
    for board in c.Win32_ComputerSystem():
        boards['Product Name'] = board.SystemFamily
    for board_id in c.Win32_BaseBoard():
        boards['UUID'] = board_id.qualifiers['UUID'][1:-1]  # 主板UUID,有的主板这部分信息取到为空值，ffffff-ffffff这样的
        if board_id.SerialNumber.strip() == '':
            boards['Serial Number'] = board_id.ConfigOptions[2]
        else:
            boards['Serial Number'] = board_id.SerialNumber  # 主板序列号
        boards['Manufacturer'] = board_id.Manufacturer  # 主板生产品牌厂家
    return boards

# 处理器
def printCPU():
    tmpdict = {}
    tmpdict["CpuCores"] = 0
    for cpu in c.Win32_Processor():
        tmpdict["cpuid"] = cpu.ProcessorId.strip()
        tmpdict["cpu_model"] = cpu.Name
        tmpdict['systemName'] = cpu.SystemName
        try:
            tmpdict["cpu_physical_count"] = cpu.NumberOfCores
        except:
            tmpdict["CpuCores"] += 1
        tmpdict["CpuClock"] = cpu.MaxClockSpeed
        tmpdict['DataWidth'] = cpu.DataWidth
    print (tmpdict)
    return  tmpdict


# 主板
def printMain_board():
    boards = {}
    # print(c.Win32_BaseBoard())
    for board_id in c.Win32_BaseBoard():
        boards['UUID'] = board_id.qualifiers['UUID'][1:-1]  # 主板UUID,有的主板这部分信息取到为空值，ffffff-ffffff这样的
        if board_id.SerialNumber.strip() == '':
            boards['Serial Number'] = board_id.ConfigOptions[2]
        else:
            boards['Serial Number'] = board_id.SerialNumber  # 主板序列号
        boards['Manufacturer'] = board_id.Manufacturer  # 主板生产品牌厂家
        boards['Product Name'] = board_id.Product  # 主板型号
    print (boards)
    return boards


# BIOS
def printBIOS():
    bioss = []
    for bios_id in c.Win32_BIOS():
        tmpmsg = {}
        tmpmsg['BiosCharacteristics'] = bios_id.BiosCharacteristics  # BIOS特征码
        tmpmsg['version'] = bios_id.Version  # BIOS版本
        tmpmsg['Manufacturer'] = bios_id.Manufacturer.strip()  # BIOS固件生产厂家
        tmpmsg['ReleaseDate'] = bios_id.ReleaseDate  # BIOS释放日期
        tmpmsg['SMBIOSBIOSVersion'] = bios_id.SMBIOSBIOSVersion  # 系统管理规范版本
        bioss.append(tmpmsg)
        print(bios_id)
    print (bioss)
    return bioss


# 硬盘
def printDisk():
    disks = []
    for disk in c.Win32_DiskDrive():
        # print disk.__dict__
        tmpmsg = {}
        tmpmsg['SerialNumber'] = disk.SerialNumber.strip()
        tmpmsg['DeviceID'] = disk.DeviceID
        tmpmsg['Caption'] = disk.Caption
        tmpmsg['Size'] = disk.Size
        tmpmsg['UUID'] = disk.qualifiers['UUID'][1:-1]
        disks.append(tmpmsg)
    for d in disks:
        print (d)
    return disks


# 内存
def printPhysicalMemory():
    memorys = []
    for mem in c.Win32_PhysicalMemory():
        tmpmsg = {}
        tmpmsg['UUID'] = mem.qualifiers['UUID'][1:-1]
        tmpmsg['BankLabel'] = mem.BankLabel
        tmpmsg['SerialNumber'] = mem.SerialNumber.strip()
        # tmpmsg['ConfiguredClockSpeed'] = mem.ConfiguredClockSpeed
        tmpmsg['Capacity'] = mem.Capacity
        # tmpmsg['ConfiguredVoltage'] = mem.ConfiguredVoltage
        memorys.append(tmpmsg)
    for m in memorys:
        print (m)
    return memorys


# 电池信息，只有笔记本才会有电池选项
def printBattery():
    isBatterys = False
    for b in c.Win32_Battery():
        isBatterys = True
    return isBatterys


# 网卡mac地址：
def printMacAddress():
    macs = []
    for n in  c.Win32_NetworkAdapter():
        mactmp = n.MACAddress
        if mactmp and len(mactmp.strip()) > 5:
            tmpmsg = {}
            tmpmsg['MACAddress'] = n.MACAddress
            tmpmsg['Name'] = n.Name
            tmpmsg['DeviceID'] = n.DeviceID
            tmpmsg['AdapterType'] = n.AdapterType
            tmpmsg['Speed'] = n.Speed
            macs.append(tmpmsg)
    print (macs)
    return macs

def main():

    printCPU()
    printMain_board()
    printBIOS()
    printDisk()
    printPhysicalMemory()
    printMacAddress()
    printBattery()

from datetime import datetime
if __name__ == '__main__':
    timeStamp = datetime.now()
    # 1590989507
    dateArray = datetime.fromtimestamp(1590989507)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    print(otherStyleTime)

