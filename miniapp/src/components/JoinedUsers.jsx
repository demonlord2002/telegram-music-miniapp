import React from "react";

export default function JoinedUsers({ users }) {
  return (
    <div className="users-box">
      <h3>Listeners</h3>

      {users.length === 0 && <div className="empty">No listeners</div>}

      {users.map((u) => (
        <div className="user-row" key={u.id}>
          <div className="circle">{u.name[0]}</div>
          <div className="uname">
            {u.name}
            {u.username && <span>@{u.username}</span>}
          </div>
        </div>
      ))}
    </div>
  );
}
