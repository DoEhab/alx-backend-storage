#!/usr/bin/env python3
"""
script to print logs
"""
from pymongo import MongoClient


def print_stats():
    """
    connecting to mongo DB
    count logs method and status
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
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


if __name__ == '__main__':
    print_stats()
