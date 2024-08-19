#!/usr/bin/env python3
from typing import Tuple


def index_range(page: int = 1, page_size: int = 10) -> Tuple[int, int]:
    """_summary_

    Returns:
        Tuple: start_index, end_index
    """
    if page < 1:
        page = 1
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
