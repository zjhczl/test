# gps授时
import socket
import threading
import time
import datetime


def time_addition(time1, time2):
    # 将时间字符串解析为时间对象
    time1_obj = datetime.datetime.strptime(time1, "%H%M%S.%f")
    time2_obj = datetime.datetime.strptime(time2, "%H%M%S.%f")

    # 将两个时间相加
    result_time = time1_obj + (time2_obj - datetime.datetime(1900, 1, 1))

    # 格式化相加后的时间为"hhmmss.ss"的格式
    formatted_time = result_time.strftime("%H%M%S.%f")[:-3]

    return formatted_time


def time_difference(time1, time2):
    # 将时间字符串解析为时间对象
    time1_obj = datetime.datetime.strptime(time1, "%H%M%S.%f")
    time2_obj = datetime.datetime.strptime(time2, "%H%M%S.%f")

    # 计算时间差值
    time_delta = time1_obj - time2_obj

    # 将时间差值转换为总秒数
    total_seconds = abs(time_delta.total_seconds())

    # 计算小时、分钟和秒数
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = total_seconds % 60

    # 格式化时间差值为"hhmmss.ss"的格式
    formatted_diff = "{:02d}{:02d}{:06.4f}".format(hours, minutes, seconds)

    return formatted_diff


# 接收机配置端
host = "192.168.1.55"
port = 21001

# host = "127.0.0.1"
# port = 9500
print("连接接收机...")
try:
    # 创建TCP套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接接收机
    sock.connect((host, port))
except socket.error as e:
    print("Socket error:", e)
except Exception as e:
    print("Error:", e)

print("接收机连接成功.")

current_time = "000000.0000"

current_time_zhen = "000000.0000"

gps_time_zhen = "000000.0000"


def printMsg():
    global current_time_zhen
    global gps_time_zhen
    while True:
        data = sock.recv(1024)
        current_time = datetime.datetime.now()
        print("----")
        print(data)
        # 将字节串转换为字符串
        data_str = data.decode("utf-8")

        # 使用split方法分割字符串
        split_data = data_str.split(',')

        # 提取时间信息
        gps_time_zhen = split_data[1]

        # 格式化时间为hhmmss.ss
        current_time_zhen = current_time.strftime("%H%M%S.%f")[:11]
        print("系统时间：")
        print(current_time_zhen)
        print("gps时间：")
        print(gps_time_zhen)
        print("")


def printTime():
    global current_time
    global current_time_zhen
    global gps_time_zhen
    while True:
        time_now = datetime.datetime.now()
        # 格式化时间为hhmmss.ss
        current_time = time_now.strftime("%H%M%S.%f")[:11]

        shijiancha = time_difference(current_time, current_time_zhen)

        gps_time = time_addition(gps_time_zhen, shijiancha)

        print(gps_time)

        time.sleep(0.001)


thread0 = threading.Thread(target=printTime)


thread1 = threading.Thread(target=printMsg)


thread1.start()
thread0.start()


while True:

    time.sleep(1)
