import React from "react";
import axios from "axios";

export default function AdminControls({ settings, chat_id }) {
  async function toggle(type) {
    await axios.get(
      `${process.env.REACT_APP_API_URL}/api/settings/toggle`,
      { params: { chat_id, key: type } }
    );
  }

  return (
    <div className="admin-controls">
      <h3>Admin Controls</h3>

      <div className="control-row">
        <span>Everyone Skip</span>
        <button onClick={() => toggle("everyone_skip")}>
          {settings.everyone_skip ? "ON" : "OFF"}
        </button>
      </div>

      <div className="control-row">
        <span>Everyone End</span>
        <button onClick={() => toggle("everyone_end")}>
          {settings.everyone_end ? "ON" : "OFF"}
        </button>
      </div>
    </div>
  );
}
