import os

# Heroku port
bind = "0.0.0.0:" + os.getenv("PORT", "8000")

# Reduce workers and threads to avoid R14 Memory quota exceeded
workers = 1        # 1 worker is enough for small apps
threads = 2        # 2 threads is safe
timeout = 120      # keep timeout if needed
