# --** coding="UTF-8" **--

##############################
###     Coded by 番茄      ###
###    @ Summer Studio     ###
##############################

import os
import time

# 时间戳(timestamp)
# 世界时UT(Universal Time) / 格林威治时间G.M.T.
# 格林威治时间1970/01/01_00-00-00起 > 至现在的总秒数
# 相当于北京时间1970/01/01_08-00-00


# 将字符串的时间转换为时间戳
def TT_Data2Stamp():
    time_a = "2017-09-06 11:22:33"
    time_a_A = time.strptime(time_a, "%Y-%m-%d %H:%M:%S")   # 时间格式区分大小写不能变
    time_a_stamp = int(time.mktime(time_a_A))
    
    print(time_a_A)
    print(time_a_stamp)


# 计算当前的TW时间
def ShowCurrentTimeOfTW():
    time_TWdata = "2016-04-30 23:59:59"
    time_TWdata_temp = time.strptime(time_TWdata, "%Y-%m-%d %H:%M:%S")
    time_TWdata_Stamp = int(time.mktime(time_TWdata_temp))

    time_now = int(time.time())   # 获取当前时间戳

    time_TW = (time_now - time_TWdata_Stamp)/60/60/24 + 1
    str_Ouput = "Current Time of TW: " + str(int(time_TW))
    print(str_Ouput)


# 计算指定的TW时间
def ShowAppointedTimeOfTW():
    time_TWdata = "2016-04-30 23:59:59"
    time_TWdata_temp = time.strptime(time_TWdata, "%Y-%m-%d %H:%M:%S")
    time_TWdata_Stamp = int(time.mktime(time_TWdata_temp))

    time_appoint = input('Input Appointed Date: ')
    time_appoint = time_appoint + ' 00:00:00'
    time_appoint_temp = time.strptime(time_appoint, "%Y-%m-%d %H:%M:%S")
    time_appoint_Stamp = int(time.mktime(time_appoint_temp))

    time_TW = (time_appoint_Stamp - time_TWdata_Stamp)/60/60/24 + 1
    str_Ouput = "Current Time of TW: " + str(int(time_TW))
    print(str_Ouput)


# 指定TW时间反推日期
def ShowDateOfTWTime():
    time_TWdata = "2016-04-30 23:59:59"
    time_TWdata_temp = time.strptime(time_TWdata, "%Y-%m-%d %H:%M:%S")
    time_TWdata_Stamp = int(time.mktime(time_TWdata_temp))

    time_TW = int(input('Input TW Time: '))
    time_TW = time_TWdata_Stamp + (time_TW*24*60*60)
    time_TW_temp = time.localtime(time_TW)

    time_date = time.strftime("%Y-%m-%d", time_TW_temp)
    str_Ouput = "Current Time of TW: " + time_date
    print(str_Ouput)


###############################
#     MAIN FUNCTION ENTRY     #
###############################
if __name__ == "__main__":
    print("------------------------------")
    print("TW Timer Mode:")
    print("------------------------------")
    print("Mode 1 >>> 计算当前的TW时间")
    print("Mode 2 >>> 计算指定的TW时间")
    print("Mode 3 >>> 指定TW时间反推日期")
    print("------------------------------")

    tMode = input('Select TW Time Mode: ')

    if tMode == '1':
        ShowCurrentTimeOfTW()
    elif tMode == '2':
        print("Input Format: 2018-05-18")
        ShowAppointedTimeOfTW()
    elif tMode == '3':
        print("Input Format: 1000")
        ShowDateOfTWTime()
    else:
        print("Error TW Time Mode")
        exit()


#------------------------------#
#    River flows in summer     #
#------------------------------#
