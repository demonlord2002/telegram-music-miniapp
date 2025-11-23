from collections import defaultdict

class DB:
    def __init__(self):
        # internal memory DB (Heroku safe as long as dyno stays alive)
        self.data = defaultdict(lambda: {
            "queue": [],
            "settings": {
                "everyone_skip": False,
                "everyone_end": False
            },
            "joined_users": {}
        })

    # ----------------------- QUEUE -----------------------
    def add_to_queue(self, chat_id, track):
        self.data[chat_id]["queue"].append(track)

    def get_queue(self, chat_id):
        return self.data[chat_id]["queue"]

    def skip_track(self, chat_id):
        if self.data[chat_id]["queue"]:
            self.data[chat_id]["queue"].pop(0)

    # ---------------------- SETTINGS ----------------------
    def get_settings(self, chat_id):
        return self.data[chat_id]["settings"]

    def toggle_setting(self, chat_id, key):
        self.data[chat_id]["settings"][key] = not self.data[chat_id]["settings"][key]

    def can_skip(self, chat_id, user_id):
        """
        Decide if user allowed to /skip
        """
        s = self.data[chat_id]["settings"]
        if s["everyone_skip"]:
            return True
        return False  # otherwise only admin (checked from bot)

    # ----------------------- USERS ------------------------
    def get_joined_users(self, chat_id):
        return list(self.data[chat_id]["joined_users"].values())

    def join_room(self, chat_id, user_id, name, username):
        self.data[chat_id]["joined_users"][user_id] = {
            "id": user_id,
            "name": name,
            "username": username
        }

    def leave_room(self, chat_id, user_id):
        if user_id in self.data[chat_id]["joined_users"]:
            del self.data[chat_id]["joined_users"][user_id]
