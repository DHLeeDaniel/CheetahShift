# ⚙️CheetahCast-App 🐆

# 🐆 (ENG)CheetahCast-App

**Let the input flow.**

CheetahCast is a lightweight, real-time input streaming utility

that mirrors your **laptop keyboard input** to any device

with a browser — including iPad, Android tablets, or even another desktop —

**with zero installation or configuration.**

---

## 🎯 Purpose of Use

- Typing practice & live captioning for presentations
- iPad as a clean secondary display
- Local input → Browser output over Wi-Fi
- No logging. No cloud. No tracking.

---

## 🛠 Technical Structure

- Python (pynput + websockets)
- HTML + JS (browser-based display)
- WebSocket-powered real-time communication
- Auto-detects Wi-Fi IP changes and reconnects seamlessly

---

## 💡 Key Features

- `sender/main.py`: Detects key input on laptop
- `receiver/index.html`: Shows real-time input on any browser
- `run.py`: Combined launcher
- `flask_app.py`: Optional web UI via local server
- No install required. Nothing is stored.

---

## 🛡 System Philosophy

> “A powerful system that never looks inside.”
> 
> 
> Your input belongs to you.
> 
> The system just lets it flow.
> 

---

## 🖥 Demo Flow

1. Run the sender on your laptop
2. Open Safari or Chrome on iPad/Android
3. Type — and watch it appear live

---

## 📦 GitHub

https://github.com/DHLeeDaniel/CheetahCast


-----


**입력을 흐르게 하라.**

CheetahCast는 노트북의 키보드 입력을

iPad·Android 태블릿, 그리고 데스크탑 노트북 등 브라우저를 띄울 수 있는 기기에서

**설치 없이, 실시간으로 시각화해주는 경량 입력 스트리밍 유틸리티**입니다.

---

## 🎯 사용 목적

- 타이핑 훈련 / 낭독 발표용 자막
- iPad 보조 출력 화면
- 로컬 감지 → 네트워크 브라우저 수신
- 입력은 기록되지 않으며, 중앙 서버 없음

---

## 🛠 기술 구조

- Python (pynput + websockets)
- HTML + JS (브라우저 출력)
- WebSocket 기반 실시간 통신
- 와이파이 변경 자동 인식 및 재연결

---

## 💡 주요 특징

- `sender/main.py`: 로컬에서 키 입력 감지
- `receiver/index.html`: 태블릿/브라우저에서 실시간 출력
- `run.py`: 통합 실행용
- `flask_app.py`: 서버를 통해 웹 UI 제공 가능
- 설치 불필요 / 기록 없음

---

## 🛡 시스템 철학

> “강력하지만, 들여다보지 않는 시스템”
> 
> 
> 키 입력은 당신의 것, 시스템은 단지 흐르게 할 뿐.
> 

---

## 🖥 시연 방식

- 노트북에서 실행 후
- 태블릿 Safari, Android Chrome 등 브라우저에서 접근
- 실시간으로 입력 반영됨

---

## 📦 GitHub 링크

https://github.com/DHLeeDaniel/CheetahCast 

# ———————————————-
🤣Humorous Version README.md

# 🐆 CheetahCast

> 당신의 노트북 키보드를 iPad, Android, 다른 브라우저 기기로 연결합니다.
> 
> 
> 설치 ❌ 설정 ❌ IP 입력 ❌ → 자동 감지로 즉시 연결.
> 

---

## ✨ 이게 뭐예요?

**CheetahCast**는 노트북의 키보드 입력을

다른 기기의 브라우저(예: iPad Safari, Android Chrome 등)에

**실시간으로 출력**해주는 초경량 WebSocket 입력 전송 시스템입니다.

- ✅ 별도 앱 설치 필요 없음
- ✅ IP 자동 인식 (와이파이 변경 시에도 자동)
- ✅ Safari, Chrome 등 브라우저만 있으면 작동

> “레노버 키보드로 아이패드에 타이핑할 수 있을까?”
> 
> 
> 이 질문에서 시작된 현실적 입력 해방 시스템.
> 

---

## ⚙️ 작동 방식

[노트북 키보드]

↓

[Python WebSocket 서버 (자동 IP 감지)]

↓

[Safari/Chrome 등 브라우저 (iPad, Android, PC)]

↓

[<textarea>에 실시간 입력 출력]

- 로컬 와이파이 환경에서 작동
- IP 변경 시에도 자동 인식하여 연결 유지
- 설치나 인증 없이 브라우저에서 바로 실행

---

## ✅ 지원 기기

- iPad (Safari)
- Android 태블릿 (Chrome)
- 다른 노트북/PC (어떤 브라우저든 OK)

> 어디든 브라우저만 있다면 입력의 목적지가 될 수 있습니다.
> 

---

## 🚀 사용 방법

1. 노트북에서 실행:

```bash
python sender/main.py

```

> http://[자동 표시된 IP 주소]:8765        👈  페이지를 열면 바로 입력 수신 대기 상태가 됩니다.
> 

---

## 🛠️ 기술 스택 & 구조

- Python (WebSocket + keyboard input)
- JavaScript (WebSocket client)
- HTML + CSS (브라우저 UI)

CheetahCast/
├── sender/       # 입력 감지 + 서버
│   └── [main.py](http://main.py/)
├── receiver/     # HTML + JS 수신기
│   ├── index.html
│   ├── app.js
│   └── style.css
├── [README.md](http://readme.md/)
└── LICENSE

## 🔐 보안 & 철학

- 우리는 시스템을 해킹하지 않습니다
- 기기에 들어가지 않습니다
- 오직 입력만 흐르게 합니다

> "We don’t hack the device. We let the input flow."
> 

---

## 📌 향후 추가 기능 (예정)

- 디바이스 인증/페어링 (토큰 기반)
- 감정 기반 입력 시각화 (Cheetah-Fin 연계)
- 모바일용 네이티브 수신기 앱

---

## 📦 GitHub 링크

https://github.com/DHLeeDaniel/CheetahCast 

## 🧪 License

MIT License

© 2025 이동훈 (Lee DongHun)

> CheetahCast – 설치 없이 타자만 흐르게.
> 
> 
> 키보드는 그대로, 입력은 어디로든.
>

