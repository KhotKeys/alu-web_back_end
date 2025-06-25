#!/usr/bin/env python3
"""Log stats from nginx collection"""

from pymongo import MongoClient

def log_stats():
    """Provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    print(f"{collection.count_documents({})} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
