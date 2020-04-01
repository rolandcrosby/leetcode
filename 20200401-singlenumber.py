from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """This implementation will only work if elements occur exactly
        once or twice in the input."""
        possible = set()
        for n in nums:
            if n in possible:
                possible.remove(n)
            else:
                possible.add(n)
        return list(possible)[0]

if __name__ == "__main__":
    testdata = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4)
    ]
    passed = 0
    for tc in testdata:
        assert Solution().singleNumber(tc[0]) == tc[1]
        passed += 1
    print("%d of %d tests passed" % (passed, len(testdata)))
