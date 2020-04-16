from utils.adb.adbutils import adbutils,keyword
import sys
from logging import Logger
import os
import re
@keyword
def get_current_activity(sn=''):
    cmd = 'dumpsys activity top | grep ACTIVITY'

    logger = Logger('AdbUtils')
    adb = adbutils(out=sys.stderr, logger=logger)
    # b'  ACTIVITY com.huawei.android.launcher/.unihome.UniHomeLauncher 1cb9757 pid=8443\r\n  ACTIVITY com.huawei.gametest.huawei/com.huawei.hms.josgame.NewApiActivity fdefcf4 pid=18926\r\n'
    res = adb.exec_shell(cmd,sn).decode('utf-8').strip()
    # print(res)
    '''按换行符划分，每行为一个activity的信息，最后面的即当前activity'''
    res = res.split(os.linesep)[-1]
    '''按空白字符划分，第二个为 包名/activity名'''
    res = res.split()[1]

    # res = adbutils().exec_shell(cmd,sn)
    print(res)
    return res

# cmd = 'devices'
# logger = Logger('AdbUtils')
# adb = adbutils(out=sys.stderr,logger=logger)
get_current_activity()