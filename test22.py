# 读取串口压缩数据并通过电台转发
import socket
import brotli


def compress_data(data):
    # 使用Brotli算法压缩数据
    compressed_data = brotli.compress(data)
    return compressed_data


def decompress_data(compressed_data):
    # 使用Brotli算法解压缩数据
    decompressed_data = brotli.decompress(compressed_data)
    return decompressed_data


# 接收机配置端
host = "192.168.3.53"
port = 2222


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


def printMsg():
    while True:
        data = sock.recv(1024)
        compressed_data = compress_data(data)
        print(compressed_data)


printMsg()
