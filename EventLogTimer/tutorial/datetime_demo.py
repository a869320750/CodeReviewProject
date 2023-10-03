# 代码来源：https://baijiahao.baidu.com/s?id=1769484471382177983&wfr=spider&for=pc
import datetime

# 获取当前日期和时间
now = datetime.datetime.now()

# 输出当前日期和时间
print("当前日期和时间：", now)

# 格式化日期和时间
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M:%S")

# 输出格式化后的日期和时间
print("格式化后的日期：", formatted_date)
print("格式化后的时间：", formatted_time)

# 将字符串转换为日期时间对象
date_str = "2023-08-24 11:45:14"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

# 输出日期时间对象
print("日期时间对象：", date_obj)

# 计算两个日期之差
date1 = datetime.datetime(2023, 6, 16, 11, 45, 14)
date2 = datetime.datetime(2022, 5, 15, 19, 19, 8)
date_diff = date1 - date2
print("两个日期的差异：", date1, date2, date_diff)

# 在特定日期上增加或减少时间量
one_week_ago = now - datetime.timedelta(weeks=1)
one_day_later = now + datetime.timedelta(days=1)
print("一周前的日期：", one_week_ago)
print("一天后的日期：", one_day_later)


# 有时候，你可能需要获取某个日期是星期几，或者某个日期所在周的起始日期和结束日期。
# Python中的**weekday()和isoweekday()**方法可以帮助你实现这个目标。
# 下面的代码演示了如何获取特定日期的周信息：
# 获取特定日期的周信息
date = datetime.datetime(2023, 6, 16)

# 获取星期几（0表示星期一，6表示星期日）
weekday = date.weekday()

# 获取所在周的起始日期和结束日期
start_of_week = date - datetime.timedelta(days=weekday)
end_of_week = start_of_week + datetime.timedelta(days=6)

# 输出结果
print("日期：", date)
print("星期几：", weekday)
print("所在周的起始日期：", start_of_week)
print("所在周的结束日期：", end_of_week)