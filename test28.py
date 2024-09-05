# TCP client
import socket
import threading
import time


def DDmm2D(ddmm):
    dd = str(ddmm).split(".")[0][0:-2]
    mm = str(ddmm).split(".")[0][-2:]+"."+str(ddmm).split(".")[1]
    dd = float(dd)
    mm = float(mm)
    d = dd + mm/60
    return d


# 接收机配置端
host = "127.0.0.1"
port = 15000

# host = "127.0.0.1"
# port = 9500
print("连接接收机...")
try:
    # 创建TCP套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接接收机
    sock.connect((host, port))
except Exception as e:
    print("Error:", e)
    exit()

print("接收机连接成功.")


def printMsg():
    while True:
        data = sock.recv(1024)
        print(data)
        time.sleep(0.1)


thread1 = threading.Thread(target=printMsg)
thread1.start()

while True:

    # 等待输入
    cmd = input()
    cmd = cmd.encode('utf-8')
    # 发送指令
    print(cmd)
    sock.send(cmd + b' \r\n')
