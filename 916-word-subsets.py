# 916. Word Subsets
# We are given two arrays A and B of words.  Each word is a string of lowercase letters.
#
# Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".
#
# Now say a word a from A is universal if for every b in B, b is a subset of a.
#
# Return a list of all universal words in A.  You can return the words in any order.
#
# Example 1:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# Output: ["facebook","google","leetcode"]
#
# Example 2:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# Output: ["apple","google","leetcode"]
#
# Example 3:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
# Output: ["facebook","google"]
#
# Example 4:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# Output: ["google","leetcode"]
#
# Example 5:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
# Output: ["facebook","leetcode"]
#
# Note:
# - 1 <= A.length, B.length <= 10000
# - 1 <= A[i].length, B[i].length <= 10
# - A[i] and B[i] consist only of lowercase letters.
# - All words in A[i] are unique: there isn't i != j with A[i] == A[j].


from typing import List, Dict
import testlib


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def chars(s: str) -> Dict[str, int]:
            n = {}
            for char in s:
                n[char] = n.setdefault(char, 0) + 1
            return n

        def subset(a: Dict[str, int], b: Dict[str, int]) -> bool:
            for k in b:
                if k not in a or a[k] < b[k]:
                    return False
            return True

        needed = {}
        for word in B:
            n = chars(word)
            for c in n:
                if c not in needed:
                    needed[c] = n[c]
                elif needed[c] < n[c]:
                    needed[c] = n[c]
        return [w for w in A if subset(chars(w), needed)]


if __name__ == "__main__":
    testdata = [
        (
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["e", "o"],
            ["facebook", "google", "leetcode"],
        ),
        (
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["l", "e"],
            ["apple", "google", "leetcode"],
        ),
        (
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["e", "oo"],
            ["facebook", "google"],
        ),
        (
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["lo", "eo"],
            ["google", "leetcode"],
        ),
        (
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["ec", "oc", "ceo"],
            ["facebook", "leetcode"],
        ),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().wordSubsets(tc[0], tc[1]), tc[2], tc),
        testdata,
    )

