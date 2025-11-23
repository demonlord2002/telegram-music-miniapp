import multiprocessing

bind = "0.0.0.0:" + os.getenv("PORT", "8000")  # Heroku port
workers = multiprocessing.cpu_count() * 2 + 1
threads = 4
timeout = 120
