#main.py
from pynput import keyboard
import asyncio
import websockets

connected_clients = set()

# 메시지 전송
async def send_to_all(message):
    for ws in connected_clients.copy():
        try:
            await ws.send(message)
        except:
            connected_clients.remove(ws)

# 키보드 이벤트 처리 (비동기 루프에서 호출)
def on_press(key):
    try:
        text = key.char
    except AttributeError:
        text = f"[{key.name}]"
    asyncio.run_coroutine_threadsafe(send_to_all(text), asyncio.get_event_loop())

# WebSocket handler
async def handler(websocket, path="/"):
    connected_clients.add(websocket)
    print(f"🟢 handler 진입 - 현재 클라이언트 수: {len(connected_clients)}")
    try:
        while True:
            await asyncio.sleep(1)  # 연결 유지
    except websockets.exceptions.ConnectionClosed:
        print("⚠️ 연결 종료")
    finally:
        connected_clients.remove(websocket)
        print(f"❌ Client disconnected. Remaining: {len(connected_clients)}")

# 메인 서버 루프
async def main():
    print("🚀 WebSocket 서버 시작: ws://0.0.0.0:8765")

    # 키보드 리스너를 백그라운드에서 실행
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # 서버 실행
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()  # 무한 대기

if __name__ == "__main__":
    asyncio.run(main())
