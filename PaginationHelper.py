# TODO: complete this class
import math


class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self._collection = collection
        self._items_per_page = items_per_page
        self._items_total = len(collection)
        self._page_count = math.ceil(self._items_total / items_per_page)

    # returns the number of items within the entire collection
    def item_count(self):
        return self._items_total

    # returns the number of pages
    def page_count(self):
        return self._page_count

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        last_index = self._page_count - 1
        if page_index > self._page_count - 1 or page_index < 0:
            return -1
        if page_index == last_index:
            items_last_page = self._items_total % self._items_per_page
            return items_last_page
        else:
            return self._items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index > self._items_total - 1 or item_index < 0 or self._items_total == 0:
            return -1
        return item_index // self._items_per_page


if __name__ == '__main__':
    helper = PaginationHelper(["a", "b"], 100)

    for i in range(0, 100):
        print(f"i: {i} | {helper.page_index(i)}")
