import os
from flask import Flask, send_from_directory, jsonify, request
from utils.db import Database
from flask_cors import CORS

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BUILD_DIR = os.path.join(BASE_DIR, "build")  # web/build

app = Flask(__name__, static_folder=BUILD_DIR, static_url_path="/")
CORS(app)

db = Database()

# ------------------------------
# Mini App API — Get room data
# ------------------------------
@app.route("/api/room/<chat_id>")
def room_data(chat_id):
    chat_id = int(chat_id)
    now_playing = db.get_now_playing(chat_id)
    queue = db.get_queue(chat_id)
    users = db.get_joined_users(chat_id)

    return jsonify({
        "now_playing": now_playing,
        "queue": queue,
        "joined_users": users
    })


# ------------------------------
# Mini App — User Join Room
# ------------------------------
@app.route("/api/join/<chat_id>", methods=["POST"])
def join_room(chat_id):
    chat_id = int(chat_id)
    payload = request.json

    user = {
        "id": payload.get("id"),
        "name": payload.get("name"),
        "username": payload.get("username"),
        "photo": payload.get("photo")
    }

    db.user_join(chat_id, user)
    return jsonify({"status": "joined"})


# ------------------------------
# Serve React Build
# ------------------------------
@app.route("/room/<chat_id>")
def room_page(chat_id):
    return send_from_directory(BUILD_DIR, "index.html")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    file_path = os.path.join(BUILD_DIR, path)
    if path != "" and os.path.exists(file_path):
        return send_from_directory(BUILD_DIR, path)
    return send_from_directory(BUILD_DIR, "index.html")


# ------------------------------
# Gunicorn Entry
# ------------------------------
if __name__ == "__main__":
    print(f"Serving from {BUILD_DIR}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
