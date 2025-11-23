import React from "react";

export default function PlayerCard({ now }) {
  if (!now)
    return (
      <div className="player-card empty">
        No song is playing…
      </div>
    );

  return (
    <div className="player-card">
      <img src={now.thumbnail} className="thumb" />
      <div className="info">
        <div className="title">{now.title}</div>
        <div className="artist">{now.artist}</div>
        <div className="dur">⏱ {now.duration}s</div>
      </div>
    </div>
  );
}
