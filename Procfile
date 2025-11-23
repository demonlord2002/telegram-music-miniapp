# Web server (FastAPI ASGI)
web: gunicorn web.server:app -w 1 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT --timeout 120

# Bot worker (Telegram bot)
worker: python bot.py
