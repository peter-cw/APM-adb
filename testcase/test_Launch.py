from unittest import TestCase
from aw.aw_launch_activity import AwLaunch
from parameterized import parameterized
class test_Launch(TestCase):
    def __init__(self):
        super.__init__()

    def setUpClass(cls) -> None:

    def setUp(self) -> None:
        pass


    def tearDown(self) -> None:
        pass

    @parameterized.expand(get_test_data())
    def test_launch_fisrt(self,pkg,activity,sn):
        gamebox_box = 'com.huawei.gamebox/com.huawei.gamebox.GameBoxActivity'
        res = AwLaunch().launch_activity_first(pkg=pkg,launcher_activity=activity,sn=sn)

    @parameterized.expand(get_test_data())
    def test_launch_cold(self,pkg,activity,sn):
        res = AwLaunch().launch_activity_cold(pkg=pkg,launcher_activity=activity,sn=sn)

    @parameterized.expand(get_test_data())
    def test_launch_hot(self,pkg,activity,sn):
        res = AwLaunch().launch_activity_hot(pkg=pkg,launcher_activity=activity,sn=sn)


def get_test_data():
    return

