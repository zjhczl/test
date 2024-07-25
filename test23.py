# 网络检测

import socket
import serial
import threading
import base64
import math
import time
import datetime

def getGGA(lat, lon):
    lat = math.floor(lat) * 100 + (lat - math.floor(lat)) * 60
    lon = math.floor(lon) * 100 + (lon - math.floor(lon)) * 60
    ggaTime = time.strftime("%H%M%S", time.gmtime(time.time()))
    gga = "GPGGA," + ggaTime + "," + \
        str(lat) + ",N," + str(lon) + ",E,3,15,2,100,M,2,M,6,0"
    # 计算校验码
    checkNum = ord(gga[0])
    for i in range(1, len(gga)):
        checkNum = checkNum ^ ord(gga[i])
    gga = "$" + gga + "*" + hex(checkNum)[2:].upper() + "\r\n"
    return gga

   
def connectCors(corsHost, corsPort, mountPoint, username, password, lat=35.103973106, lon=117.409903771):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((corsHost, corsPort))
    except Exception:
        print("连接cors失败")
        return 0
    request = f"GET /{mountPoint} HTTP/1.0\r\n"
    request += f"Host: {corsHost}:{corsPort}\r\n"
    request += f"User-Agent: NTRIP connect\r\n"
    request += f'Authorization: Basic {base64.b64encode(f"{username}:{password}".encode()).decode()}\r\n'
    request += "Ntrip-Version: Ntrip/2.0\r\n"
    request += "\r\n"
    client_socket.sendall(request.encode())
    # 接收并打印服务器响应
    response = client_socket.recv(1024)
    print(response)
    # 第三步：计算并发送GGA数据
    gga = getGGA(lat, lon)
    client_socket.send(gga.encode('utf-8'))
    # 接收并打印流数据
    t = datetime.datetime.now().timestamp()
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        
        # print( datetime.datetime.now().timestamp()-t)
        print(datetime.datetime.now())
        if(int(datetime.datetime.now().timestamp()-t)>=2):
            print("网络中断。。。")
        t = datetime.datetime.now().timestamp()
        
        gga = getGGA(lat, lon)
        client_socket.send(gga.encode('utf-8'))
    # 关闭连接
    client_socket.close()

corsHost = "sss.top"
corsPort = 28002
mountPoint = "khhha"
username = "kuaja"
password = "12kjkj3"

connectCors(corsHost, corsPort, mountPoint, username,
                password)
