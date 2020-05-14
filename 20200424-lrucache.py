# LRU Cache
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It should
# support the following operations: get and put.
#
# - get(key) - Get the value (will always be positive) of the key if the key exists in
# the cache, otherwise return -1.
# - put(key, value) - Set or insert the value if the key is not already present. When
# the cache reached its capacity, it should invalidate the least recently used item
# before inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

import testlib
from collections import OrderedDict
from typing import List, Tuple, Optional


class MyOrderedDict:
    def __init__(self):
        self._nodes = {}
        self._order = []

    def __contains__(self, key):
        return key in self._nodes

    def __getitem__(self, key):
        if key not in self:
            raise KeyError("invalid key: {}".format(key))
        self.move_to_end(key)
        return self._nodes[key]

    def __setitem__(self, key, value):
        if key not in self._nodes:
            self._order.append(key)
        self._nodes[key] = value

    def move_to_end(self, key):
        if key not in self:
            raise KeyError("invalid key: {}".format(key))
        self._order.pop(self._order.index(key))
        self._order.append(key)

    def popitem(self, last=False):
        if len(self._order) == 0:
            raise KeyError("empty dict")
        if last:
            idx = self._order.pop(-1)
        else:
            idx = self._order.pop(0)
        item = self._nodes[idx]
        del self._nodes[idx]
        return item


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._used = 0
        self._storage = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self._storage:
            return -1
        self._storage.move_to_end(key)
        return self._storage[key]

    def put(self, key: int, value: int) -> None:
        if key in self._storage:  # update, no accounting
            self._storage[key] = value
            self._storage.move_to_end(key)
            return
        if self._used == self._capacity:  # need to evict oldest
            self._storage.popitem(False)
            self._storage[key] = value
            return
        # otherwise we have space to add another item
        self._storage[key] = value
        self._used += 1


def example_test(t: testlib.unittest.TestCase):
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    t.assertEqual(cache.get(1), 1)
    cache.put(3, 3)
    t.assertEqual(cache.get(2), -1)
    cache.put(4, 4)
    t.assertEqual(cache.get(1), -1)
    t.assertEqual(cache.get(3), 3)
    t.assertEqual(cache.get(4), 4)


if __name__ == "__main__":
    testdata = [
        [
            ("new", (2,), None),
            ("put", (1, 1), None),
            ("put", (2, 2), None),
            ("get", (1,), 1),
            ("put", (3, 3), None),
            ("get", (2,), -1),
            ("put", (4, 4), None),
            ("get", (1,), -1),
            ("get", (3,), 3),
            ("get", (4,), 4),
        ],
        [
            ("new", (2,), None),
            ("put", (2, 1), None),
            ("put", (1, 1), None),
            ("put", (2, 3), None),
            ("put", (4, 1), None),
            ("get", (1,), -1),
            ("get", (2,), 3),
        ],
    ]

    def execute(
        t: testlib.unittest.TestCase, statements: List[Tuple[str, Tuple, Optional[int]]]
    ):
        obj = None
        for (instruction, args, expected) in statements:
            if instruction == "new":
                obj = LRUCache(args[0])
            elif instruction == "put":
                obj.put(args[0], args[1])
            elif instruction == "get":
                res = obj.get(args[0])
                if expected is not None:
                    t.assertEqual(res, expected)

    testlib.run(lambda t, tc: execute(t, tc), testdata)
