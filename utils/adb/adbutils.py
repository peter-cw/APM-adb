from utils.confutils.ConfUtils import CfUtils
from utils.pathutils import pathutils
from logging import Logger
import subprocess
import sys

class adbutils():
    global ANDROID_SDK
    cur_path = pathutils.get_parent_path()
    cf = CfUtils(cur_path + '/conf.ini')
    ANDROID_SDK = cf.get('project_conf','android_sdk')
    global ADB_PATH
    ADB_PATH  = ANDROID_SDK+'/platform-tools/adb.exe'
    global device
    device = cf.get('project_conf','cur_device')
    global output
    output = None
    global logger
    cur_logger = None

    def __init__(self,out,logger):
        global output
        output = out
        global loggers
        cur_loggers = logger

    @classmethod
    def exec_shell(cls,cmd:str,shell=True):

        cmd_str = ADB_PATH + ' -s ' + device+' '
        if shell:
            cmd_str += ' shell '
        cmd_str +=  cmd
        print(cmd_str)
        # subprocess.check_call()
        try:
            res = subprocess.check_output(cmd_str,stderr=subprocess.STDOUT,shell=False)
            return res


            cls.logger.log('execute cmd:%r  successfully,return: %r'%(cmd_str,res))

        except subprocess.CalledProcessError as exc:
            cls.cur_logger.error('returncode:%r'%exc.returncode)
            cls.cur_logger.error('cmd:%r'% exc.cmd)
            cls.cur_logger.error('output:%r'% exc.output)


cmd = 'devices'
logger = Logger('AdbUtils')
adb = adbutils(out=sys.stderr,logger=logger)
res = adbutils.exec_shell(cmd,shell=False)
print(res.decode('utf-8').split('\n')[1].split('\t')[0])
