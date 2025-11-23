import React, { useEffect, useState } from "react";
import axios from "axios";
import PlayerCard from "../components/PlayerCard";
import QueueList from "../components/QueueList";
import JoinedUsers from "../components/JoinedUsers";
import AdminControls from "../components/AdminControls";
import WebApp from "@twa-dev/sdk";

export default function Room() {
  const urlParams = new URLSearchParams(window.location.search);
  const chat_id = urlParams.get("chat_id");
  const user = WebApp.initDataUnsafe.user;

  const [room, setRoom] = useState(null);

  const api = axios.create({
    baseURL: `${process.env.REACT_APP_API_URL}`
  });

  async function joinRoom() {
    await api.get(`/api/join`, {
      params: {
        chat_id,
        user_id: user.id,
        name: user.first_name,
        username: user.username || ""
      }
    });
  }

  async function loadRoom() {
    const r = await api.get(`/api/room`, { params: { chat_id } });
    setRoom(r.data);
  }

  useEffect(() => {
    joinRoom();
    loadRoom();

    const interval = setInterval(loadRoom, 3000);
    return () => clearInterval(interval);
  }, []);

  if (!room) return <div className="loading">Loading…</div>;

  return (
    <div className="room-container">
      <PlayerCard now={room.queue[0]} />

      <QueueList queue={room.queue} />

      <JoinedUsers users={room.users} />

      <AdminControls settings={room.settings} chat_id={chat_id} />
    </div>
  );
}
