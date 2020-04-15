import os
import sys
import platform

class pathutils():
    @staticmethod
    def get_current_path():
        '''

        :return: the absolute path of current file
        '''
        print('***获取当前目录***')
        path1 = os.getcwd()
        # path2 = os.path.abspath(os.path.dirname(__file__))
        print(path1)
        # print(path2)
        return path1

    @staticmethod
    def get_parent_path():
        '''

        :return: the absolute path of current file's parent directory
        '''

        print('***获取上级目录***')
        # print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
        # print(os.path.abspath(os.path.dirname(os.getcwd())))
        path = os.path.abspath(os.path.join(os.getcwd(), ".."))
        print(path)
        return path

    @staticmethod
    def get_grandpa_path():
        '''

        :return: the absolute path of current file's parent directory's parent directory
        '''
        print('***获取上上级目录***')
        # print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
        path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
        print(path)
        return path

    @staticmethod
    def get_grep():
        grep_str = None
        cur_platform = platform.platform()
        if 'Windows' in cur_platform:
            grep_str = 'findStr'
        elif 'Linux' in cur_platform:
            grep_str = 'grep'
        else:
            pass
        print('current platform:{}'.format(cur_platform))
        return grep_str

# p1 = platform.platform()
# print(p1)
# platform = sys.platform
# print(platform)
print(pathutils.get_grep())