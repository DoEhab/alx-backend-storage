#!/usr/bin/env python3
"""
script to print logs
"""
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.logs
db_collection = db.nginx
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print(f"{db_collection.count_documents({})} logs")

print("Methods:")
for method in methods:
    count = db_collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

status_check = db_collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_check} status check")
