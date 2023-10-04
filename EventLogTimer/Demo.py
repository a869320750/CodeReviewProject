import os
import DataAccessLayer as dal
import datetime

current_directory = os.path.dirname(os.path.abspath(__file__))
print(current_directory)
file_path = os.path.join(current_directory, 'EventData.csv')

erd = dal.EventRecordData(file_path)
print(erd.getDataFrame().tail())


# 数据录入
event_title = 'Dota'
event_content = ''
start_time = datetime.datetime(2023,10,5,0,00,0)
duration = datetime.timedelta(hours=3, minutes=0)
end_time = start_time + duration
event_type = '休息'
# 数据录入

MyDict = ({
        'EventTitle':event_title,
        'EventContent':event_content,
        'StartTime':start_time,
        'Duration':duration,
        'EndTime':end_time,
        'Type':event_type
        })

erd.appendRow(MyDict)


print(erd.getDataFrame().tail())