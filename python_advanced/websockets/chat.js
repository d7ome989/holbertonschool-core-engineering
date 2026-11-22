const messages = document.getElementById("messages");
const input = document.getElementById("message-input");
const button = document.getElementById("send-button");

const socket = new WebSocket("ws://localhost:8000/ws");

function addMessage(text, type) {
    const div = document.createElement("div");
    div.textContent = text;
    div.className = "message " + type;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
}

socket.onopen = () => {
    addMessage("Connected to server", "system");
};

socket.onclose = () => {
    addMessage("Connection lost", "system");
};

socket.onmessage = (event) => {
    addMessage("Server: " + event.data, "received");
};

function sendMessage() {
    const text = input.value;
    if (text === "") {
        return;
    }
    socket.send(text);
    addMessage("You: " + text, "sent");
    input.value = "";
}

button.onclick = sendMessage;

input.onkeydown = (event) => {
    if (event.key === "Enter") {
        sendMessage();
    }
};
