#!/usr/bin/env python3
"""
function insert_school
"""


def schools_by_topic(mongo_collection, topic):
    """
    insert a new doc
    :param mongo_collection: DB Collection
    :param topic: specific topic
    """
    result = mongo_collection.find({"topics": topic})
    return list(result)
