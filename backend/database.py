from pymongo import MongoClient

MONGO_URI = ""

client = MongoClient(MONGO_URI)

db = client["ai_website_generator"]

sessions_collection = db["sessions"]
