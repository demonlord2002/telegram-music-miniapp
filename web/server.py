from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from utils.db import DB

db = DB()

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# ---------------- API ROUTES ----------------

@app.get("/api/room")
def get_room(chat_id: int):
    """
    MiniApp fetches room info (queue + users)
    """
    return {
        "queue": db.get_queue(chat_id),
        "users": db.get_joined_users(chat_id),
        "settings": db.get_settings(chat_id)
    }

@app.get("/api/join")
def join_room(chat_id: int, user_id: int, name: str, username: str = None):
    """
    User joins MiniApp room
    """
    db.join_room(chat_id, user_id, name, username)
    return {"status": "joined"}

@app.get("/api/leave")
def leave_room(chat_id: int, user_id: int):
    """
    User leaves room
    """
    db.leave_room(chat_id, user_id)
    return {"status": "left"}

# ---------------- NON-API ROUTES FOR FRONTEND ----------------

@app.get("/room")
def room_redirect(chat_id: int):
    """
    Redirect or render room page (for Mini App join)
    """
    return {
        "queue": db.get_queue(chat_id),
        "users": db.get_joined_users(chat_id),
        "settings": db.get_settings(chat_id)
    }

@app.get("/")
def home():
    return {"status": "OK", "message": "Music MiniApp Backend Running"}

@app.get("/favicon.ico")
def favicon():
    return ""

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    uvicorn.run(
        "web.server:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=False
    )
