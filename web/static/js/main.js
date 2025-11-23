const urlParams = new URLSearchParams(window.location.search);
const chatId = urlParams.get("chat_id");

document.getElementById("chat-id").innerText = chatId;

const API_BASE = "/api";

async function fetchRoom() {
    const res = await fetch(`${API_BASE}/room?chat_id=${chatId}`);
    const data = await res.json();

    // Settings
    document.getElementById("settings").innerText = 
        `Everyone Skip: ${data.settings.everyone_skip}, Everyone End: ${data.settings.everyone_end}`;

    // Users
    const userList = document.getElementById("user-list");
    userList.innerHTML = "";
    data.users.forEach(user => {
        const li = document.createElement("li");
        li.textContent = user.name + (user.username ? ` (@${user.username})` : "");
        userList.appendChild(li);
    });

    // Queue
    const queueList = document.getElementById("queue-list");
    queueList.innerHTML = "";
    data.queue.forEach((song, index) => {
        const li = document.createElement("li");
        li.textContent = `${index+1}. ${song.title || "Unknown"} (${song.duration || "0:00"})`;
        li.onclick = () => playSong(song.url);
        queueList.appendChild(li);
    });
}

const audioPlayer = document.getElementById("audio-player");

function playSong(url) {
    audioPlayer.src = url;
    audioPlayer.play();
}

document.getElementById("play-next").onclick = async () => {
    const res = await fetch(`${API_BASE}/room?chat_id=${chatId}`);
    const data = await res.json();
    if (data.queue.length > 0) {
        playSong(data.queue[0].url);
    }
};

fetchRoom();
setInterval(fetchRoom, 5000); // auto-refresh every 5s
