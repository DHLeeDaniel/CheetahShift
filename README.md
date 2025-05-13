# CheetahShift 🐆  
**입력을 흐르게 하라.**

CheetahShift는 노트북의 키보드 입력을  
iPad·Android 태블릿 등 브라우저를 띄운 기기에서  
**설치 없이, 실시간으로 시각화해주는 경량 입력 스트리밍 유틸리티**입니다.

---

## 🎯 사용 목적

- 🧠 **타이핑 훈련 / 낭독 발표** 시 실시간 자막처럼 사용
- 📱 **iPad나 태블릿을 보조 출력 화면**처럼 활용
- 🔐 **중앙 기록 없이**, 사용자의 로컬에서만 감지되고 전송됨

> 키 입력은 **로컬에서 감지되고** → **동일 네트워크 상의 디바이스**로만 스트리밍됩니다.  
> 입력 기록은 저장되지 않으며, 클라이언트는 오직 '수신자' 역할만 수행합니다.

---

## 🛠 기능 요약

- 💻 **Sender** (`sender/`): `main.py` 실행 → 키보드 입력 감지 + WebSocket 서버
- 📱 **Receiver** (`receiver/`): `index.html` 실행 → 입력 실시간 수신 + 출력
- 🔁 **Wi-Fi 이동 시 자동 재연결** 지원
- 🌐 **브라우저 기반 출력** → Safari, Chrome 등 설치 불필요

---

## 📁 디렉토리 구조

cheetah_shift/
├── sender/ # Python 기반 WebSocket 송신기
│ └── main.py
├── receiver/ # HTML + JS 수신기 (브라우저용 UI)
│ └── index.html
├── webapp/ # (예정) GitHub Pages 또는 배포용 정적 웹 리소스
├── flask_app.py # (선택) HTML 제공용 Flask 서버
├── run.py # Sender + Web UI 동시 실행 스크립트

---

## ✅ 사용 방법

1. **노트북에서 실행**
```bash
python sender/main.py

iPad 또는 Android 태블릿 브라우저에서 접속

http://<노트북 IP>:8000 또는

로컬 HTML 열기 (receiver/index.html)

실시간 입력 확인


-----

✅ 같은 Wi-Fi에 연결만 되어 있다면 작동합니다.
❌ 인터넷 연결 필요 없음.
❌ 설치도 필요 없음.

🛡 개인정보 & 보안
❌ 중앙 서버 없음

❌ 키 입력 기록 없음

✅ 모든 전송은 휘발성, 로컬 메모리 기반

✅ 와이파이 기반 → 사용자가 직접 통제 가능

📦 라이선스
MIT
