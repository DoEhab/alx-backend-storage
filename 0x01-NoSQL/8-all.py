#!/usr/bin/env python3
"""
function list_all
"""


def list_all(mongo_collection):
    """
    list all docs
    :param mongo_collection:
    :return: doc list
    """
    return list(mongo_collection.find())
