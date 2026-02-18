from pymongo import MongoClient
import os

# Logic: Default local MongoDB connection string
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

try:
    # Initialize the client
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    
    # Define your database and collection
    db = client["greybox_hospital"]
    beds_collection = db["live_beds"]  # This will store current bed status
    
    # Trigger a connection check
    client.server_info() 
    print("✅ Connected to local MongoDB successfully.")
except Exception as e:
    print(f"🚨 MongoDB Connection Failed: {e}")
    client = None
    db = None
    beds_collection = None