from utils.adb.adbutils import adbutils
class AwLaunch(object):

    global adb

    def __init__(self):
        if self.__class__.adb != None:
            self.adb = self.__class__.adb
        else:
            self.__class__.adb = adbutils()
            self.adb = self.__class__.adb

    def launch_activity_first(self,pkg,launcher_activity,sn=None):
        # adb = adbutils()
        self.adb.exec_shell(cmd='pm clear '+pkg, shell=True, sn=None)
        res = self.adb.start_activity(activity=launcher_activity,sn=sn)
        return res


    def luanch_activity_hot(self,pkg,launcher_activity,sn=None):
        # adb = adbutils()
        res = self.adb.start_activity(activity=launcher_activity,sn=sn)
        self.adb.exec_shell(cmd='input keyevent KEYCODE_HOME', shell=True, sn=None)
        res = self.adb.start_activity(activity=launcher_activity)
        print('热启动', res)
        return res

    def luanch_activity_cold(self, pkg,launcher_activity, sn=None):
        # adb = adbutils()
        res = self.adb.start_activity(activity=launcher_activity,sn=sn)
        res = self.adb.stop_activity(pkg='com.huawei.gamebox')
        res = self.adb.start_activity(activity=launcher_activity)
        print('冷启动', res)
        return res

