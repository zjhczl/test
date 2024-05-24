# ntrip caster改进版本

import socket
import serial
import threading
import base64
import math
import time
import json
import re
import logging


class NtripCaster:

    def __init__(self, serverHost, serverPort):
        self.serverHost = serverHost
        self.serverPort = serverPort
        self.server_socket = ""
        self.ntripServer = ""
        self.clients = []
        self.users = []

    def addNtripServer(self, host, port):
        self.ntripServer = (host, port)
        pass

    def addUser(self, userName, passWord):

        self.users.append(base64.b64encode(
            f"{userName}:{passWord}".encode()).decode())

        pass

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.serverHost, self.serverPort))
        self.server_socket.listen(30)
        print(f"Ntrip Caster started on {self.serverHost}:{self.serverPort}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(
                f"New client connected: {client_address[0]}:{client_address[1]}")
            client_thread = threading.Thread(
                target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):

        self.clients.append(client_socket)

        try:
            data = client_socket.recv(1024)
            print(data)
            if not data:
                print(data)
                print("没有接收到数据")
                client_socket.close()
                self.clients.remove(client_socket)

            # 处理接收到的数据
            jsonStr = data.decode("utf-8").replace("\r\n",
                                                   ",").replace(" ", "").replace(",,", ",")

            rule = re.compile('Authorization:Basic(.*?),')
            authorization = re.findall(rule, jsonStr)[0]
            print(jsonStr)
            print(authorization)
            if authorization in self.users:
                response = 'ICY 200 OK\r\n'
                print(response)
                client_socket.send(response.encode())
            else:
                print("authorization failed")
                client_socket.close()
                self.clients.remove(client_socket)
                return 0

        except Exception:
            print(Exception)

        self.process_data(client_socket)
        client_socket.close()
        self.clients.remove(client_socket)

    def process_data(self, caster_socket):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(self.ntripServer)
            # 接收并打印流数据
            while True:

                data = client_socket.recv(1024)
                if not data:
                    break
                print(data)
                try:
                    caster_socket.send(data)
                    # data = caster_socket.recv(1024)
                    # if not data:
                    #     break
                    # print("接受到的数据：")
                    # print(data)
                except Exception:
                    print(Exception)
                    print("caster send data err")
                    break

            # 关闭连接
            client_socket.close()
            # 在这里处理接收到的数据
            # 可以根据Ntrip协议解析数据、转发数据等操作
        except Exception:
            print(Exception)
            print("can not connect ntrip server")
            # caster_socket.send(b" can not connect ntrip server")

            return 0
