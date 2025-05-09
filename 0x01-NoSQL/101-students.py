#!/usr/bin/env python3
"""
function top_students
"""


def top_students(mongo_collection):
    """
    get top students
    :param mongo_collection: DB Collection
    """
    return mongo_collection.aggregate([
        {'$addFields': {'averageScore': {'$avg': "$topics.score"}}},
        {'$sort': {'averageScore': -1}}
    ])
