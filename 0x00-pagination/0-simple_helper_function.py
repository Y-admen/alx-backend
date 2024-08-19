#!/usr/bin/env python3
from typing import Tuple


def index_range(page: int = 1, page_size: int = 0) -> Tuple[int, int]:
    """_summary_

    Returns:
        Tuple: start_index, end_index
    """
    if page < 1 or page_size < 1:
        raise ValueError("ValueError")
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)
