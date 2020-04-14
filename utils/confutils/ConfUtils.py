import configparser
import os
from utils.pathutils import pathutils
class CfUtils():
    def __init__(self,fp:str,flush=True):
        '''

        :param fp: ini file path
        :type fp:str
        :param flush: if want to write to ini file immediatelly
        :type flush: bool
        '''
        if not os.path.isfile(fp):
            raise ValueError('%r is not a ini file'%fp)

        self.cf = configparser.ConfigParser()
        # if isinstance(fp,file):
        #     cf.read_file(fp)
        self.fp = fp
        self.flush = flush
        self.cf.read(fp,encoding='utf-8')

    def has_option(self,section,option):
        return  self.cf.has_option(section,option)

    def has_section(self,section):
        return  self.cf.has_section(section)

    def get(self,section,option):

        value = self.cf.get(section,option)
        print(value)
        return value

    def set(self,section,option,value):
        if not self.cf.has_section(section):
            self.cf.add_section(section)
        self.cf.set(section,option,value)
        if self.flush:
            self.write()
        # with open(self.fp,'w',encoding='utf-8') as f:
        #     self.cf.write(f)

    def sections(self):
        return  self.cf.sections()

    def options(self,section):
        return  self.cf.options(section)

    def add_section(self,section):
        self.cf.add_section(section)
        if self.flush:
            self.write()

    def remove_section(self,section):
        self.cf.remove_section(section)
        if self.flush:
            self.write()

    def remove_option(self,section,option):
        self.cf.remove_option(section,option)
        if self.flush:
            self.write()

    def write(self):
        with open(self.fp,'w',encoding='utf-8') as f:
            self.cf.write(f)
# f = open('test.zip')
# # f.read()
# print(type(f))



cur_path = pathutils.get_parent_path()
cf = CfUtils(cur_path+'/conf.ini')
cf.remove_option('test_sec','test_op1')
# cf.set('test_sec','test_op1','1234')
# cf.set('test_sec','test_op2','abc')
# cf.write()

