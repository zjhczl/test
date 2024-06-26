# 电台转发差分信号
import socket
import serial
import threading
import base64
import math
import time
import brotli


def compress_data(data):
    # 使用Brotli算法压缩数据
    compressed_data = brotli.compress(data)
    return compressed_data


def decompress_data(compressed_data):
    # 使用Brotli算法解压缩数据
    decompressed_data = brotli.decompress(compressed_data)
    return decompressed_data


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

    print("连接串口")
    # ser = serial.Serial('/dev/ttyUSB0', 115200)
    ser = serial.Serial("/dev/tty.usbserial-210", 115200)
    # 接收并打印流数据
    while True:
        data = client_socket.recv(1024)

        if not data:
            break
        # print("start")
        # print(data)
        # print("------------")
        compressed_data = compress_data(data)
        print(compressed_data)
        # print("------------")

        # print(decompress_data(compressed_data))
        # print("------------")
        # print("end")
        ser.write(compressed_data+b"\n")
        gga = getGGA(lat, lon)
        client_socket.send(gga.encode('utf-8'))

    # 关闭连接
    client_socket.close()


corsHost = "10.58.32.10"
corsPort = 8001
mountPoint = "RTCM33_GRCEJ"
username = "kuangka"
password = "123"
lat = 35.103973106
lon = 117.409903771
connectCors(corsHost, corsPort, mountPoint, username,
            password, lat, lon)
