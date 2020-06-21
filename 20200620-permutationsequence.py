# Permutation Sequence
# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following
# sequence for n = 3:
#
# "123" 000
# "132" 001
# "213" 010
# "231" 011
# "312" 100
# "321" 101
# Given n and k, return the kth permutation sequence.
#
# Note:
# - Given n will be between 1 and 9 inclusive.
# - Given k will be between 1 and n! inclusive.
#
# Example 1:
# Input: n = 3, k = 3
# Output: "213"
#
# Example 2:
# Input: n = 4, k = 9
# Output: "2314"

import testlib


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Use factorial permutation indices as described here:
        # https://www.keithschwarz.com/interesting/code/?dir=factoradic-permutation
        # or here:
        # https://py.checkio.org/mission/reversed-permutation-index/publications/sjosef23/python-3/some-more-magic-and-factorials/share/473022125e05dd4f79c8e51f4a67b4fe/
        idx = k - 1
        facs = [1] * n
        for i in range(3, n + 1):
            facs[n - i] = facs[n - i + 1] * (i - 1)

        indices_in_remaining = []
        for fac in facs:
            digit = idx // fac
            indices_in_remaining.append(digit)
            idx -= digit * fac

        digits = list(range(1, n + 1))
        out = ""
        for i in indices_in_remaining:
            out += str(digits.pop(i))
        return out


if __name__ == "__main__":
    testdata = [(4, 9, "2314"), (3, 3, "213")]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().getPermutation(tc[0], tc[1]), tc[2], tc),
        testdata,
    )
