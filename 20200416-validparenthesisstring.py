# Valid Parenthesis String
# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
#
# - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# - Any right parenthesis ')' must have a corresponding left parenthesis '('.
# - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
#
# Example 1:
# Input: "()"
# Output: True
#
# Example 2:
# Input: "(*)"
# Output: True
#
# Example 3:
# Input: "(*))"
# Output: True
#
# Note:
# The string size will be in the range [1, 100].

import testlib
from typing import List


class Solution:
    def checkValidString(self, s: str) -> bool:
        # Iterate over the string from the left, checking if
        # we ever have more )s than (s and *s:
        closing = 0
        other = 0
        for c in s:
            if c == ")":
                closing += 1
            else:
                other += 1
            if closing > other:
                return False

        # Then iterate from the right, looking for (s that can't
        # be balanced:
        opening = 0
        other = 0
        for c in reversed(s):
            if c == "(":
                opening += 1
            else:
                other += 1
            if opening > other:
                return False

        return True


if __name__ == "__main__":
    testdata = [
        ("()", True),
        ("(*)", True),
        ("(*))", True),
        (")(", False),
        ("(*()", True),
        ("(())((())()()(*)(*()(())())())()()((()())((()))(*", False),
        ("", True),
        (
            "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())",
            False,
        ),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().checkValidString(tc[0]), tc[1], tc),
        testdata,
    )
