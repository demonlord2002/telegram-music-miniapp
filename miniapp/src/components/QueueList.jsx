import React from "react";

export default function QueueList({ queue }) {
  return (
    <div className="queue-box">
      <h3>Queue</h3>
      {queue.length === 0 && <div className="empty">No songs</div>}

      {queue.map((t, i) => (
        <div className="queue-item" key={i}>
          <span className="index">{i + 1}.</span>
          <span className="q-title">{t.title}</span>
        </div>
      ))}
    </div>
  );
}
