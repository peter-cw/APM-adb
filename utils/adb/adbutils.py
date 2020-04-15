from utils.confutils.ConfUtils import CfUtils
from utils.pathutils import pathutils
from logging import Logger
import subprocess
import sys
import os
from utils.decorators.keyword import  keyword


class adbutils():
    global ANDROID_SDK
    cur_path = pathutils.get_parent_path()
    cf = CfUtils(cur_path + '/conf.ini')
    ANDROID_SDK = cf.get('project_conf','android_sdk')
    global ADB_PATH
    ADB_PATH  = ANDROID_SDK+os.path.sep+'platform-tools'+os.path.sep+'adb.exe'
    global device
    device = cf.get('project_conf','cur_device')
    global output
    output = None
    global logger
    cur_logger = None

    def __init__(self,out,logger):
        # global output
        self.output = out
        # global loggers
        self.cur_logger = logger

    # @classmethod
    @keyword
    def exec_shell(self,cmd:str,shell=True,sn=None):

        cmd_str = ADB_PATH
        if sn:
            cmd_str += ' -s ' + sn+' '
        if shell:
            cmd_str += ' shell '
        cmd_str +=  ' '+cmd
        print(cmd_str)
        # subprocess.check_call()
        try:
            res = subprocess.check_output(cmd_str,stderr=subprocess.PIPE,shell=False)
            return res


            self.cur_logger.info('execute cmd:%r  successfully,return: %r'%(cmd_str,res))

        except subprocess.CalledProcessError as exc:
            self.cur_logger.error('returncode:%r'%exc.returncode)
            self.cur_logger.error('cmd:%r'% exc.cmd)
            self.cur_logger.error('output:%r'% exc.output)


    # @classmethod
    @keyword
    def get_devices(self):
        cmd = 'devices'
        res_encode = self.exec_shell(cmd=cmd,shell=False)
        # res_encode = res_encode.rstrip()
        # print('去除首尾空白字符',res_encode)
        res_decode = res_encode.decode('utf-8')
        '''去除返回值末尾的空白字符\r,\t,\n'''
        res_decode = res_decode.strip()
        # print('去除首尾空白字符',res_decode)
        device_list = res_decode.split(os.linesep)
        '''去除'List of devices attached'标题  '''
        title = device_list.pop(0)
        # print(device_list)
        device_list = list(map(lambda x:x.split('\t')[0],device_list))
        return device_list


    # @classmethod
    @keyword
    def get_meminfo(self,sn,pkg):
        '''在命令行中可以执行，在代码中执行报错
        cmd:   adb -s 2GX0119327000343  shell  dumpsys meminfo com.huawei.hwid|findStr TOTAL
        '''
        # cmd = 'dumpsys meminfo '+pkg+'|'+pathutils.get_grep()+' TOTAL '
        '''安卓使用linux内核，故使用grep，但grep在windows平台不被识别，以字符串形式拼接'''
        cmd = '\"dumpsys meminfo '+pkg+'|grep TOTAL\" '

        res = self.exec_shell(cmd=cmd,shell=True,sn=sn)
        return res.decode('utf-8')

    @keyword
    def get_cpuinfo(self,sn,pkg):
        '''在命令行中可以执行，在代码中执行报错
        cmd:   adb -s 2GX0119327000343  shell  dumpsys meminfo com.huawei.hwid|findStr TOTAL
        '''
        # cmd = 'dumpsys meminfo '+pkg+'|'+pathutils.get_grep()+' TOTAL '
        '''安卓使用linux内核，故使用grep，但grep在windows平台不被识别，以字符串形式拼接'''
        cmd = '\"dumpsys meminfo '+pkg+'|grep TOTAL\" '

        res = self.exec_shell(cmd=cmd,shell=True,sn=sn)
        return res.decode('utf-8')

cmd = 'devices'
logger = Logger('AdbUtils')
adb = adbutils(out=sys.stderr,logger=logger)
# res = adbutils.exec_shell(cmd,shell=False)
res = adb.get_devices()
print(res)
res = adb.get_meminfo(sn=res[0],pkg='com.huawei.hwid')
print(res)
# print(res.decode('utf-8').split('\n')[1].split('\t')[0])


# def get_men(pkg_name):
#     cmd = "adb shell  dumpsys  meminfo %s" % (pkg_name)
#     print(cmd)
#     men_s = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
#     for info in men_s:
#         if len(info.split()) and info.split()[0].decode() == "TOTAL":
#             # print("men="+info.split()[1].decode())
#             men.append(int(info.split()[1].decode()))
#             print("----men----")
#             print(men)
#             return men

