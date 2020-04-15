import unittest

from typing import List, Callable, Tuple, TypeVar, Iterable

class TestLeetcode(unittest.TestCase):
    pass

T = TypeVar('T')
def run(fn: Callable[[unittest.TestCase, T], bool], testdata: Iterable[T]):
    def runTest(self):
        passed = 0
        for el in testdata:
            fn(self, el)
            passed += 1
        print("%d of %d tests passed" % (passed, len(testdata)))
    TestLeetcode.runTest = runTest
    unittest.main('testlib')