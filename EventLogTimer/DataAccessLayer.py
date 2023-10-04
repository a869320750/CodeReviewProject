# 主要是对文件的操作，实现一些增删改查的基础功能
import pandas as pd
import os
import datetime

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

class EventRecordData:
    def __init__(self, file_path:str):
        self.__file_path = file_path
# 增
    def appendRow(self, eventDataDict:dict):
        df = pd.read_csv(self.__file_path)

        new_row = pd.Series(eventDataDict)
        df.loc[len(df)] = new_row

        df.to_csv(self.__file_path, index=False)
# 查
    def getDataFrame(self):
        df = pd.read_csv(self.__file_path)
        return df
# 删除    
    def deleteRow(self, index:int):
        df = pd.read_csv(self.__file_path)
        df.drop(index, axis=0, inplace=True)
        df.to_csv(self.__file_path, index=False)
# 改    
    def updateRow(self, index:int, eventDataDict:dict):
        df = pd.read_csv(self.__file_path)
        new_row = pd.Series(eventDataDict)
        df.loc[index] = new_row
        df.to_csv(self.__file_path, index=False)
# 写入文件
    def writeFile(self, dataFrame:pd.DataFrame):
        dataFrame.to_csv(self.__file_path, index=False)