class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        gridSet = defaultdict(set)

        rows, cols = len(board), len(board[0])
        row, col = 0, 0

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == '.':
                    continue
                if (board[row][col] in rowSet[row]) or (board[row][col] in colSet[col]) or (board[row][col] in gridSet[(row//3, col//3)]):
                    return False

                rowSet[row].add(board[row][col])
                colSet[col].add(board[row][col])
                gridSet[(row//3, col//3)].add(board[row][col])

                col += 1
            row += 1

        return True