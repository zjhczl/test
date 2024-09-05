# tcp server
import socket
import time


def start_server(host='0.0.0.0', port=15002):
    # 创建一个TCP/IP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定套接字到地址和端口
    server_socket.bind((host, port))

    # 监听连接
    server_socket.listen(5)
    print(f'Server listening on {host}:{port}')

    while True:
        # 接受客户端连接
        client_socket, client_address = server_socket.accept()
        print(f'Connection from {client_address}')

        try:
            while True:
                # 向客户端发送数据
                client_socket.sendall(b'hello\n')
                print(f'Sent "hello" to {client_address}')
                time.sleep(1)  # 每秒发送一次
        except (BrokenPipeError, ConnectionResetError):
            print(f'Client {client_address} disconnected')
        finally:
            client_socket.close()


if __name__ == '__main__':
    start_server()
