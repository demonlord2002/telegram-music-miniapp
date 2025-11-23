# 🚀 Telegram Music Bot + MiniApp Deployment Guide (Heroku)

This guide will help you deploy the Telegram Music Bot + Web MiniApp on **Heroku** easily.

---

# ✅ 1. Requirements
Before starting, make sure you have:

- Python 3.10+
- Node.js 18+
- Telegram Bot Token (from @BotFather)
- API ID & API HASH (from https://my.telegram.org)
- MongoDB URI (MongoDB Atlas recommended)
- Heroku account
- Git installed

---

# ✅ 2. Project Folder Structure

Make sure your repo looks like this:

```
Procfile
runtime.txt
requirements.txt
bot.py
.gitignore
.env.example

utils/
  db.py
  spotify_api.py
  helpers.py

web/
  server.py
  gunicorn_conf.py
  build/
    index.html

miniapp/
  package.json
  public/
    index.html
  src/
    index.jsx
    App.jsx
    pages/
      Room.jsx
    components/
      PlayerCard.jsx
      QueueList.jsx
      JoinedUsers.jsx
      AdminControls.jsx
    styles/
      main.css

docs/
  deployment.md
```

---

# ✅ 3. Install Dependencies (Local)

### 📌 Install Python packages
```
pip install -r requirements.txt
```

### 📌 Build the React MiniApp

```
cd miniapp
npm install
npm run build
```

After build, a folder named `dist/` will be created.

Copy **all files inside** `dist/` into:

```
web/build/
```

---

# ✅ 4. Create Heroku App

```
heroku create my-music-bot
```

---

# ✅ 5. Set Heroku Config Vars

```
heroku config:set BOT_TOKEN=your_bot_token
heroku config:set API_ID=your_api_id
heroku config:set API_HASH=your_api_hash
heroku config:set MONGO_URI=your_mongo_uri
heroku config:set WEBHOOK_URL=https://my-music-bot.herokuapp.com
```

---

# ✅ 6. Deploy to Heroku

```
git add .
git commit -m "Initial deploy"
git push heroku main
```

Heroku will automatically:

- Install Python dependencies  
- Start the **web server** using gunicorn  
- Start the **bot worker** (bot.py)

---

# ✅ 7. Set Webhook (Optional)

```
https://api.telegram.org/bot<BOT_TOKEN>/setWebhook?url=https://my-music-bot.herokuapp.com/webhook
```

Replace `<BOT_TOKEN>` and the Heroku URL.

---

# ✅ 8. Test Everything

### Open MiniApp:
```
https://my-music-bot.herokuapp.com
```

### Test Bot Commands in Telegram:
/start  
/play song name  
/settings  

---

# ✅ 9. View Heroku Logs

```
heroku logs --tail
```

---

# 🎉 DONE!

Your Telegram Music MiniApp + Bot is successfully deployed on Heroku.
