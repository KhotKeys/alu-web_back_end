#!/usr/bin/env python3
"""Log stats from nginx collection"""

from pymongo import MongoClient


def log_stats():
    """Provides stats about Nginx logs stored in MongoDB"""
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Print total logs
    log_count = collection.count_documents({})
    print(f"{log_count} logs")

    # Print method counts
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"    method {method}: {method_count}")

    # Print status check count
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    log_stats()
