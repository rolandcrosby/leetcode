# First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index.
# If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

import testlib
from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        candidates = OrderedDict()
        for (i, c) in enumerate(s):
            if c not in seen:
                seen.add(c)
                candidates[c] = i
            elif c in candidates:
                del candidates[c]
        if len(candidates) > 0:
            (c, i) = candidates.popitem(False)
            return i
        else:
            return -1


if __name__ == "__main__":
    testdata = [("leetcode", 0), ("loveleetcode", 2), ("aabbcc", -1)]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().firstUniqChar(tc[0]), tc[1], tc),
        testdata,
    )
