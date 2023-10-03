import pandas as pd
import datetime
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
print(current_directory)
file_path = os.path.join(current_directory, 'EventData.csv')

def appendRow(eventDataDict):
    df = pd.read_csv(file_path)
    print(df)

    # new_row = pd.Series({
    #     'EventTitle':'开发EventLogTimer',
    #     'EventContent':'学习Pandas和datetime知识',
    #     'StartTime':datetime.datetime(2023,10,3,14,0,0),
    #     'Duration':datetime.timedelta(hours=3),
    #     'EndTime':datetime.datetime(2023,10,3,14,0,0) + datetime.timedelta(hours=3),
    #     })
    
    new_row = pd.Series(eventDataDict)

    df.loc[len(df)] = new_row
    print(df)

    target_path = os.path.join(file_path)
    df.to_csv(target_path, index=False)

MyDict = ({
        'EventTitle':'开发EventLogTimer',
        'EventContent':'学习Pandas和Datetime',
        'StartTime':datetime.datetime(2023,10,3,14,0,0),
        'Duration':datetime.timedelta(hours=3.5),
        'EndTime':datetime.datetime(2023,10,3,14,0,0) + datetime.timedelta(hours=3.5),
        })
appendRow(MyDict)