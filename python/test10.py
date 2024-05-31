# websocket
import asyncio
import websockets


async def handle_client(websocket, path):
    # 当新的WebSocket连接建立时，该函数将被调用
    print("New client connected")

    try:
        while True:
            # 从客户端接收消息
            message = await websocket.recv()
            print(f"Received message: {message}")

            # 发送消息给客户端
            response = f"Received: {message}"
            await websocket.send(response)
            print(f"Sent response: {response}")

    except websockets.exceptions.ConnectionClosedOK:
        # 当WebSocket连接关闭时，该异常将被捕获
        print("Client disconnected")

# 启动WebSocket服务器
start_server = websockets.serve(handle_client, "0.0.0.0", 9500)
print("server:localhost:9500")
# 运行事件循环
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
