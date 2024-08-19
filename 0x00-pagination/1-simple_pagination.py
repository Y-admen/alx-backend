#!/usr/bin/env python3
from typing import Tuple, List
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate page of the dataset based on the given page and page_size.

        Args:
            page (int, optional): Page number (default is 1).
            page_size (int, optional): Number of rows per page (default is 10).

        Returns:
            List[List]: Paginated list of rows.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        start_idx, end_idx = index_range(page, page_size)
        return self.dataset()[start_idx:end_idx]

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the start and end indexes for pagination.

    Args:
        page (int): Page number.
        page_size (int): Number of rows per page.

    Returns:
        Tuple[int, int]: Start index and end index.
    """
    total_rows = len(Server.dataset())
    start_idx = (page - 1) * page_size
    end_idx = min(start_idx + page_size, total_rows)
    return start_idx, end_idx
