# Course Schedule
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first
# take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for
# you to finish all courses?
#
# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0
#              you should also have finished course 1. So it is impossible.
#
# Constraints:
# - The input prerequisites is a graph represented by a list of edges, not adjacency
#   matrices. Read more about how a graph is represented.
# - You may assume that there are no duplicate edges in the input prerequisites.
# - 1 <= numCourses <= 10^5

import testlib
from typing import List
from pprint import pp


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) < 2:
            return True
        dependencies = {}
        for p in prerequisites:
            course = p[0]
            prereq = p[1]
            dependencies.setdefault(course, set()).add(prereq)
        unchecked = set(range(numCourses))
        checked = set()
        in_progress = set()

        def has_cycle(c: int) -> bool:
            if c in checked:
                return False
            unchecked.remove(c)
            in_progress.add(c)
            for neighbor in dependencies.get(c, set()):
                if neighbor in checked:
                    continue
                if neighbor in in_progress:
                    return True
                if has_cycle(neighbor):
                    return True
            in_progress.remove(c)
            checked.add(c)
            return False

        while unchecked:
            cur = next(iter(unchecked))
            if has_cycle(cur):
                return False
        return True


if __name__ == "__main__":
    testdata = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [[0, 1], [0, 2], [1, 2]], True),
        (4, [[0, 1], [3, 1], [1, 3], [3, 2]], False),
        (8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]], True),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().canFinish(tc[0], tc[1]), tc[2], tc),
        testdata,
    )
