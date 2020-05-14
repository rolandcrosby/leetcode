# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any
# positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1. Those numbers for which
# this process ends in 1 are happy numbers.
#
# Example:
#
# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1


class Solution:
    def isHappy(self, n: int) -> bool:
        """Naive implementation that just keeps track of all seen values and
        doesn't do any clever cycle detection."""

        def sumSquaresDigits(num: int) -> int:
            acc = 0
            while num > 0:
                acc += (num % 10) * (num % 10)
                num = num // 10
            return acc

        seen = set([n])
        while n != 1:
            n = sumSquaresDigits(n)
            if n in seen:
                return False
            seen.add(n)
        return True


class FloydSolution:
    """Fancy solution using Floyd's Tortoise and Hare algorithm (which I just
    learned about) to detect a cycle without requiring any additional space."""

    def isHappy(self, n: int) -> bool:
        def sumSquaresDigits(num: int) -> int:
            acc = 0
            while num > 0:
                digit = num % 10
                acc += digit * digit
                num = num // 10
            return acc

        slow = fast = n
        while fast != 1:
            fast = sumSquaresDigits(sumSquaresDigits(fast))
            slow = sumSquaresDigits(slow)
            if fast == slow:
                return False
        return True


if __name__ == "__main__":
    testdata = [(0, False), (1, True), (2, False), (7, True), (19, True)]
    for klass in [Solution, FloydSolution]:
        passed = 0
        for tc in testdata:
            assert klass().isHappy(tc[0]) == tc[1]
            passed += 1
        print("%s: %d of %d tests passed" % (klass.__name__, passed, len(testdata)))
