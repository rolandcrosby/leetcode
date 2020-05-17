# Find All Anagrams in a String
# Given a string s and a non-empty string p, find all the start indices of p's anagrams
# in s.
#
# Strings consists of lowercase English letters only and the length of both strings s
# and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# Example 2:
# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

import testlib
from typing import List, Dict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        needed_letters: Dict[str, int] = {}
        for c in p:
            needed_letters[c] = needed_letters.get(c, 0) + 1

        test_letters: Dict[str, int] = {}
        for c in s[0:len(p)]:
            test_letters[c] = test_letters.get(c, 0) + 1

        found: List[int] = []
        for i in range(1 + len(s) - len(p)):
            if needed_letters == test_letters:
                found.append(i)
            if i + len(p) < len(s) and s[i] != s[i + len(p)]:
                test_letters[s[i + len(p)]] = test_letters.get(s[i + len(p)], 0) + 1
                test_letters[s[i]] -= 1
                if test_letters[s[i]] == 0:
                    del test_letters[s[i]]
        return found




if __name__ == "__main__":
    testdata = [
        ("abab", "ab", [0, 1, 2]),
        ("cbaebabacd", "abc", [0, 6]),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().findAnagrams(tc[0], tc[1]), tc[2], tc),
        testdata,
    )
