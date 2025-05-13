// main.js

  const status = document.getElementById('status');
  const output = document.getElementById('output');

  let socket;

  function connect() {
    const protocol = location.protocol === "https:" ? "wss" : "ws";
    const host = location.hostname;
    const wsUrl = `${protocol}://${host}:8765`;

    socket = new WebSocket(wsUrl);

    console.log("🔌 Connecting to", wsUrl);

    socket.onopen = () => {
      console.log("✅ WebSocket connected");
      status.textContent = "✅ Connected to CheetahShift!";
      output.value = ""; // 초기화
    };

    socket.onmessage = (event) => {
      const data = event.data;
      if (["[ping]", "[cmd]", "[shift]", "[ctrl]", "[alt]"].includes(data)) return;

      output.value += data;
      output.scrollTop = output.scrollHeight;
    };

    socket.onclose = () => {
      console.log("❌ WebSocket closed");
      status.textContent = "🔄 Reconnecting...";
      retryConnect();
    };

    socket.onerror = (error) => {
      console.error("⚠️ WebSocket error:", error);
      status.textContent = "⚠️ WebSocket error.";
    };
  }

  function retryConnect() {
    setTimeout(() => {
      console.log("🔁 Retrying connection...");
      connect(); // 재연결 시도
    }, 2000); // 2초 후 재연결
  }

  // 와이파이 바뀌거나 브라우저 IP 바뀌었을 때도 재연결 시도
  setInterval(() => {
    if (!socket || socket.readyState !== WebSocket.OPEN) {
      console.log("📡 Connection inactive, trying to reconnect...");
      connect();
    }
  }, 5000); // 5초마다 체크

  connect(); // 최초 실행


