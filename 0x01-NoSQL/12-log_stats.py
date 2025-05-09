#!/usr/bin/env python3
"""
script to print logs
"""
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.logs
db_collection = db.nginx
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print(db_collection.count_documents({}))
print("Methods:")

for method in methods:
    result = db_collection.count_documents({"method": method})
    print(f"\tmethod {method}: {result}")

result = db_collection.count_documents({"method": "GET", "path": "/status"})
print(f"{result} status check")
