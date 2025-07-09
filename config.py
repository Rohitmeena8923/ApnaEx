import os
from os import getenv

# Telegram API config
API_ID = int(os.environ.get("API_ID", "27775431"))
API_HASH = os.environ.get("API_HASH", "b70bb1d45a1d05236671d4cc615e40f9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Violation_indiabot")
BOT_TEXT = "Violation_indiabot"
OWNER_ID = int(os.environ.get("OWNER_ID", "6414266397"))

# Channels and logging
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002446676469"))         # Log Channel
CHANNEL_ID2 = int(os.environ.get("CHANNEL_ID2", "-1002446676469"))       # Force Join Channel
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002446676469"))     # Optional Premium log channel

# MongoDB
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://Rohitmeena64:Ajmeer234590577@cluster0.mae8oyn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Admin and Bot Extras
ADMIN_BOT_USERNAME = "Violation_indiabot"  # without @
THUMB_URL = os.environ.get("THUMB_URL", "https://josephscollege.ac.in/wp-content/uploads/2022/04/1.jpg")

# Optional features
join = '<a href="https://t.me/+MgPgCAPUOVU2Yjhl">✳️ JOIN BACKUP</a>'
UNSPLASH_ACCESS_KEY = 'RabDRmuXXBobanmwwbvpP5LwoG4J8ox34y5Sstz-9jk'
UNSPLASH_QUERY = 'animal baby'