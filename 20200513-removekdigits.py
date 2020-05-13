# Remove K Digits
# Given a non-negative integer num represented as a string, remove k digits from the
# number so that the new number is the smallest possible.
#
# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
#
# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is
# the smallest.
#
# Example 2:
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must
# not contain leading zeroes.
#
# Example 3:
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which
# is 0.


import testlib


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        digits = list(num)
        while digits and k > 0:
            while digits[0] == "0":
                digits.pop(0)
            if k >= len(digits):
                return "0"
            try:
                # If there's a zero after k or fewer digits, remove those digits
                first_zero = digits.index("0", 0, k + 1)
                digits = digits[first_zero:]
                k -= first_zero
            except ValueError:
                # Find the greatest digit that isn't less than a digit before it
                i = 0
                while i + 1 < len(digits):
                    if digits[i + 1] < digits[i]:
                        break
                    i += 1
                digits.pop(i)
                k -= 1
        while digits and digits[0] == "0":
            digits.pop(0)
        if not digits:
            return "0"
        return "".join(digits)


if __name__ == "__main__":
    testdata = [
        ("2454", 1, "244"),
        ("10", 1, "0"),
        ("10", 2, "0"),
        ("10200", 1, "200"),
        ("20546", 1, "546"),
        ("11112", 1, "1111"),
        ("1432219", 1, "132219"),
        ("1432219", 2, "12219"),
        ("1432219", 3, "1219"),
        ("245", 1, "24"),
        ("2456", 1, "245"),
        ("2546", 1, "246"),
        ("20546", 2, "46"),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().removeKdigits(tc[0], tc[1]), tc[2], tc),
        testdata,
    )
