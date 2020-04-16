from utils.adb.adbutils import adbutils,keyword

@keyword
def get_meminfo(sn, pkg):
    '''在命令行中可以执行，在代码中执行报错
    cmd:   adb -s 2GX0119327000343  shell  dumpsys meminfo com.huawei.hwid|findStr TOTAL
    '''
    # cmd = 'dumpsys meminfo '+pkg+'|'+pathutils.get_grep()+' TOTAL '
    '''安卓使用linux内核，故使用grep，但grep在windows平台不被识别，以字符串形式拼接'''
    cmd = 'dumpsys meminfo ' + pkg + '|grep TOTAL'

    res = adbutils().exec_shell(cmd=cmd, sn=sn)
    return res.decode('utf-8')

