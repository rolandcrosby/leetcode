# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
# 
# Each letter in the magazine string can only be used once in your ransom note.
# 
# Note:
# You may assume that both strings contain only lowercase letters.
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

import testlib

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = list(magazine)
        for c in ransomNote:
            try:
                available.remove(c)
            except:
                return False
        return True

if __name__ == "__main__":
    testdata = [
        ("a", "b", False),
        ("aa", "ab", False),
        ("abc", "bacc", True)
    ]
    testlib.run(lambda t, tc: t.assertEqual(Solution().canConstruct(tc[0], tc[1]), tc[2], tc), testdata)