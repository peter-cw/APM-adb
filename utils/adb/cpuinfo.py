from utils.adb.adbutils import  keyword,adbutils
import os


@keyword
def get_cpuinfo_dumpsys(self, sn, pkg):
    '''在命令行中可以执行，在代码中执行报错
    cmd:   adb -s 2GX0119327000343  shell  dumpsys meminfo com.huawei.hwid|findStr TOTAL
    '''
    # cmd = 'dumpsys meminfo '+pkg+'|'+pathutils.get_grep()+' TOTAL '
    '''安卓使用linux内核，故使用grep，但grep在windows平台不被识别，以字符串形式拼接'''
    cmd = 'dumpsys cpuinfo ' + pkg + '|grep TOTAL '

    res = adbutils().exec_shell(cmd=cmd, sn=sn)
    return res.decode('utf-8')

@keyword
def get_cpuinfo_top(self, sn, pkg):
    '''在命令行中可以执行，在代码中执行报错
    cmd:   adb -s 2GX0119327000343  shell  dumpsys meminfo com.huawei.hwid|findStr TOTAL
    '''
    # cmd = 'dumpsys meminfo '+pkg+'|'+pathutils.get_grep()+' TOTAL '
    '''安卓使用linux内核，故使用grep，但grep在windows平台不被识别，以字符串形式拼接'''
    cmd = 'top -n 1 -s cpu' + pkg + '|grep TOTAL '

    res = adbutils().exec_shell(cmd=cmd, sn=sn).decode('utf-8')
    cpu_num = get_cpu_num(sn=sn)
    '''多核需除以CPU个数'''
    res = res/cpu_num
    return res


@keyword
def get_cpu_num(sn=''):
    ''' to get cpu number of target android smartphone
    :usage: calculate cpu utilization
    :param sn: sn of test android smartphone
    :return: cpu number of target android smartphone
    '''
    cmd = 'cat /proc/cpuinfo | grep processor'
    res = adbutils().exec_shell(cmd=cmd, sn=sn).decode('utf-8')
    res = res.strip()
    processor_list = res.split(os.linesep)
    # print(processor_list)
    return len(processor_list)