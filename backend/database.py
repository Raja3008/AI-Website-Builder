from pymongo import MongoClient

MONGO_URI = "mongodb+srv://mrajashekar482_db_user:VOMvHR31aFPDyxvu@cluster0.ceywd3f.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["ai_website_generator"]

sessions_collection = db["sessions"]
