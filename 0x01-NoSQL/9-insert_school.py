#!/usr/bin/env python3
"""
function insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert a new doc
    :param mongo_collection:
    :return: doc list
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
