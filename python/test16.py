# 一个socket流转多个
import socket
import threading

# 服务器地址和端口
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

# 存储客户端连接
clients = []

# 锁定机制，确保线程安全
lock = threading.Lock()


def handle_client(client_socket):
    global clients
    while True:
        try:
            # 接收数据
            data = client_socket.recv(1024)
            if not data:
                break

            # 打印接收到的数据
            print(f"Received: {data.decode('utf-8')}")

            # 将数据转发给所有连接的客户端
            with lock:
                for client in clients:
                    if client != client_socket:
                        try:
                            client.send(data)
                        except:
                            clients.remove(client)
        except:
            break

    with lock:
        clients.remove(client_socket)
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_HOST, SERVER_PORT))
    server.listen(5)
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        with lock:
            clients.append(client_socket)

        client_handler = threading.Thread(
            target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()
