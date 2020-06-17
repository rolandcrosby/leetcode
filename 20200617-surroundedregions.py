# Surrounded Regions
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded
# by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border
# of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not
# connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if
# they are adjacent cells connected horizontally or vertically.

from typing import List, Tuple
from collections import deque
import testlib


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) < 3 or len(board[0]) < 3:
            # nothing can be surrounded on a board smaller than 3 x 3,
            # so nothing to do here
            return
        for r in range(len(board)):
            for c in [0, len(board[0]) - 1]:
                if board[r][c] == "O":
                    self.flood_fill(board, (r, c), "o")
        for c in range(len(board[0])):
            for r in [0, len(board) - 1]:
                if board[r][c] == "O":
                    self.flood_fill(board, (r, c), "o")

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "o":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"

    def flood_fill(
        self, board: List[List[str]], start: Tuple[int, int], new_value: str
    ) -> None:
        r, c = start
        old_value = board[r][c]
        max_r = len(board) - 1
        max_c = len(board[0]) - 1
        todo = deque()
        todo.append(start)
        while todo:
            r, c = todo.popleft()
            if board[r][c] == old_value:
                board[r][c] = new_value
                if r > 0 and board[r - 1][c] == old_value:
                    todo.append((r - 1, c))
                if r < max_r and board[r + 1][c] == old_value:
                    todo.append((r + 1, c))
                if c > 0 and board[r][c - 1] == old_value:
                    todo.append((r, c - 1))
                if c < max_c and board[r][c + 1] == old_value:
                    todo.append((r, c + 1))


if __name__ == "__main__":

    def run(t: testlib.unittest.TestCase, tc: Tuple[List[List[str]], List[List[str]]]):
        board = tc[0]
        Solution().solve(board)
        t.assertEqual(board, tc[1])

    testdata = [
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
        ),
        (
            [
                ["X", "X", "O", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ],
            [
                ["X", "X", "O", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ],
        ),
    ]
    testlib.run(run, testdata)
