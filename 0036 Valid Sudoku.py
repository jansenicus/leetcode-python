class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """

        https://leetcode.com/problems/valid-sudoku/
        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(0, 9):
            for c in range(0, 9):

                current = board[r][c]

                if current == ".":
                    continue

                if current in rows[r] or current in cols[c] or current in squares[r // 3, c // 3]:
                    return False

                rows[r].add(current)
                cols[c].add(current)
                squares[r // 3, c // 3].add(current)

        return True
