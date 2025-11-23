import multiprocessing
import os

bind = "0.0.0.0:" + os.getenv("PORT", "8000")
workers = 1  # low memory dyno
threads = 2  # enough for basic concurrency
timeout = 120
