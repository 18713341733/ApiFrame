'''
a = datetime.datetime.now()
#当前时间 格式2020-8-12
today = datetime.date.today()
futher_time = datetime.date.today() + datetime.timedelta(days=30)
'''
import datetime
import time

#获取current时间戳
def get_Date(date):
    c = date.strftime('%Y-%m-%d %H:%M:%S') #变成格式 2020-8-12 00:00:00
    # 转为时间数组
    timeArray = time.strptime(c, "%Y-%m-%d %H:%M:%S")
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    return timeStamp
#获取当天凌晨零点时间戳
def get_time():
    day_time = int(time.mktime(datetime.date.today().timetuple()))
    return day_time

def get_timestamp_spec_time(clock, days=0):
    """
    获取指定的时间点的时间戳
    :param clock: 钟点;指定的时间,比如当天的凌晨一点,钟点即为1(24小时制)
    :param days:  与当前时间的相差的日期。-1 表示昨天；0 表示当天(默认)；1 表示明天
    :return:      返回时间戳
    """
    nowTime = datetime.datetime.now() + datetime.timedelta(days=days)
    specified_time = nowTime.strftime("%Y-%m-%d") + " {}:59:59".format(clock)
    timeArray = time.strptime(specified_time, "%Y-%m-%d %H:%M:%S")
    return time.mktime(timeArray)

def get_time_spec_time(clock, days=0):
    """
    获取指定的时间点的时间戳
    :param clock: 钟点;指定的时间,比如当天的凌晨一点,钟点即为1(24小时制)
    :param days:  与当前时间的相差的日期。-1 表示昨天；0 表示当天(默认)；1 表示明天
    :return:      返回时间 2022-07-28 23:59:59
    """
    nowTime = datetime.datetime.now() + datetime.timedelta(days=days)
    specified_time = nowTime.strftime("%Y-%m-%d") + " {}:59:59".format(clock)
    return specified_time


#获取current时间yyyy_MM
def get_Date_yyyy_MM(date):
    c = date.strftime('%Y-%m') #变成格式 2020-8
    return c

#获取current时间戳,不需要传参
def get_DateCurrent():
    return int(time.mktime(time.localtime(time.time())))

#根据时间维度获取当前月或当前日
def get_date(statistics_type):
    # 获取当前时间
    now_time = datetime.datetime.now()
    # 格式化时间字符串
    if statistics_type == 1:
        return now_time.strftime("%Y-%m-%d")
    else:
        return now_time.strftime("%Y-%m")



if __name__ == "__main__":
    nowTime = datetime.datetime.now() + datetime.timedelta(days=1)
    specified_time = nowTime.strftime("%Y-%m-%d") + " {}:59:59".format(23)
    print(specified_time)