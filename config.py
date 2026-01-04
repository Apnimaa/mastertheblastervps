from os import getenv

API_ID = int(getenv("API_ID", "27433400"))
API_HASH = getenv("API_HASH", "1a286620de5ffe0a7d9b57e604293555")
BOT_TOKEN = getenv("BOT_TOKEN", "7411163939:AAFDtzfzu2u7-cZkMn6qv7EHem6uZobDMDQ")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6201066540").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://niravpatel180503_db_user:vjWNaWhRk0gMSNyQ@cluster0.26bfgmf.mongodb.net/?appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1003182485007")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003182485007"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "20"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
WEBSITE_URL = getenv("WEBSITE_URL", None)
AD_API = getenv("AD_API", None)
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
SECONDS = 300  # for example, a 5-minute delay
