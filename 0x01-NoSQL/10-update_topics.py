#!/usr/bin/env python3
"""
function insert_school
"""


def update_topics(mongo_collection, name, topics):
    """
    insert a new doc
    :param mongo_collection: DB Collection
    :param name: school name to update
    :param topics: list of topics
    """
    mongo_collection.update_many(
        {"name": name},
        {"Sset": {"topics": topics}}
    )
