# CheetahShift

# CheetahShift 🐆

**입력을 흐르게 하라.**

CheetahShift는 노트북 키보드 입력을 iPad 등 기기의 브라우저에서  
**설치 없이 실시간으로 출력**해주는 경량 유틸리티 시스템입니다.

---

## 🎯 기능 요약

- 💻 **Sender**: 노트북 키보드 입력을 감지해 WebSocket으로 전송
- 📱 **Receiver**: Safari 등 브라우저에서 입력을 실시간 수신
- 🔐 설치 및 인증 절차 없이 로컬 네트워크 상에서 동작

---

## 🛠 디렉토리 구조
cheetah_shift/
├── sender/ # Python 기반 WebSocket 송신기
├── receiver/ # HTML + JS 수신기 (브라우저용)
├── webapp/ # (예정) GitHub Pages용 Web UI


---

## ✅ 사용 방법

1. `sender/main.py` 실행 (노트북)
2. `receiver/index.html` 실행 (브라우저)
3. 동일 네트워크 내에서 실시간 입력 확인

---

## 📦 라이선스

MIT

