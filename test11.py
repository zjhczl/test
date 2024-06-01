# socket转websocket

import asyncio
import websockets
import socket


async def socket_to_websocket(websocket, path):
    try:
        # 创建Socket连接
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(socket_server)
        sock.sendall(b"1")
        while True:
            # 从Socket接收数据
            socket_data = sock.recv(1024)
            print(socket_data)
            if not socket_data:
                break

            # 发送数据到WebSocket客户端
            await websocket.send(socket_data)

            # # 从WebSocket客户端接收数据
            # websocket_data = await websocket.recv()
            # print(websocket_data)
            # if not websocket_data:
            #     break

            # # 发送数据回Socket服务器
            # sock.sendall(websocket_data)

    except Exception as e:
        print("Error:", e)

    finally:
        # 关闭Socket连接
        sock.close()


if __name__ == "__main__":
    # Socket服务器的地址和端口
    socket_server = ("192.168.10.50", 9500)

    # WebSocket服务器的地址和端口
    websocket_server = "0.0.0.0"
    websocket_port = 9000

    # 启动WebSocket服务器
    print("websocket server:0.0.0.0:9000")

    start_server = websockets.serve(
        socket_to_websocket, websocket_server, websocket_port)

    # 运行事件循环
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
