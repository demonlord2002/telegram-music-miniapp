from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "MusicMiniApp")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]


class Database:

    # ---------------------------
    # SONG QUEUE
    # ---------------------------
    def add_song(self, chat_id, track):
        db.queues.update_one(
            {"chat_id": chat_id},
            {"$push": {"songs": track}},
            upsert=True
        )

    def get_queue(self, chat_id):
        data = db.queues.find_one({"chat_id": chat_id})
        return data.get("songs", []) if data else []

    def clear_queue(self, chat_id):
        db.queues.update_one(
            {"chat_id": chat_id},
            {"$set": {"songs": []}},
            upsert=True
        )

    # ---------------------------
    # JOINED USERS
    # ---------------------------
    def user_join(self, chat_id, user):
        db.joins.update_one(
            {"chat_id": chat_id},
            {"$addToSet": {"users": user}},
            upsert=True
        )

    def get_joined_users(self, chat_id):
        data = db.joins.find_one({"chat_id": chat_id})
        return data.get("users", []) if data else []

    # ---------------------------
    # SETTINGS
    # ---------------------------
    def get_settings(self, chat_id):
        data = db.settings.find_one({"chat_id": chat_id})
        if not data:
            return {"allowed": "admins"}
        return data

    def set_settings(self, chat_id, allowed):
        db.settings.update_one(
            {"chat_id": chat_id},
            {"$set": {"allowed": allowed}},
            upsert=True
        )

    # ---------------------------
    # ROOM INFO
    # ---------------------------
    def set_now_playing(self, chat_id, track):
        db.now_playing.update_one(
            {"chat_id": chat_id},
            {"$set": {"track": track}},
            upsert=True
        )

    def get_now_playing(self, chat_id):
        data = db.now_playing.find_one({"chat_id": chat_id})
        return data.get("track") if data else None
      
