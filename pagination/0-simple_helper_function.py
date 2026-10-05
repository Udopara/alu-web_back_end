#!/usr/bin/env python3
""" Simple helper function module for pagination index calculation.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for the given
    pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
