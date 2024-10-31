import os
import yaml
class getFileData:
    def __init__(self):
        pass
    def get_yaml_data(self,name):
        """
        返回yaml文件数据
        :param name: 读取yaml文件数据
        :return:
        """

        #数据文件路径
        file_path='F:/PYDEMO/appTest/appAutoTest/data/'+name
        #file_path=os.getcwd()+os.sep+"data"+os.sep+name
        with open (file_path,"r",encoding='utf-8') as f:
            return yaml.safe_load(f)
