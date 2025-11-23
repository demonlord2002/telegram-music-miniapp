import React from "react";
import PlayerCard from "../components/PlayerCard";
import QueueList from "../components/QueueList";
import JoinedUsers from "../components/JoinedUsers";
import AdminControls from "../components/AdminControls";

export default function Room() {
  return (
    <div className="room">
      <PlayerCard />
      <QueueList />
      <JoinedUsers />
      <AdminControls />
    </div>
  );
}
