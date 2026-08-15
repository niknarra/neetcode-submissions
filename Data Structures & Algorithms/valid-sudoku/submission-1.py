class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boxSet = defaultdict(set)

        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == '.':
                    continue
                
                if (board[row][col] in rowSet[row]) or (board[row][col] in colSet[col]) or (board[row][col] in boxSet[(row//3, col//3)]):
                    return False
                
                rowSet[row].add(board[row][col])
                colSet[col].add(board[row][col])
                boxSet[(row//3, col//3)].add(board[row][col])
    
        return True