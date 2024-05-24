# ubuntu串口连接

import serial
import threading
import time
import datetime


def printMsg(ser):
    while True:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)


print("连接串口")
ser = serial.Serial('/dev/ttyUSB0', 115200)


my_thread = threading.Thread(target=printMsg, args=(ser,))

# 启动线程
my_thread.start()

while True:

    # 等待输入
    cmd = input()
    if (cmd == "exit"):
        break
    cmd = cmd.encode('utf-8')
    # 发送指令
    print(cmd)
    ser.write(cmd + b' \r\n')

    # # 发送指令
    # current_time = str(datetime.datetime.now())+"-"
    # ser.write(current_time.encode('utf-8') +
    #           b'dasdhasjkdhaskljdc;aLvj"SJopssssafj okljlkjlksjdasdjsddfsdfsd ;kzbasjdhaskjdhaskljdnlkadjlkasjkal \r\n')
    # time.sleep(1)


# 等待线程结束
my_thread.join()
