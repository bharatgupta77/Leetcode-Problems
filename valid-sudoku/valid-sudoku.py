class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                     continue

                if num in rows[i] or num in cols[j] or num in subgrids[i // 3][j // 3]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                subgrids[i // 3][j // 3].add(num)

        return True
        