class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chess = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        def check_valid(row, col):
            for c in [i for i in range(n) if i != col]:
                if chess[row][c] == 'Q':
                    return False
            for r in [i for i in range(n) if i != row]:
                if chess[r][col] == 'Q':
                    return False
            base_row, base_col = max(row-col, 0), max (col-row, 0)
            for acc in range(0, n - abs(row - col)):
                if base_row+acc != row:
                    if chess[base_row+acc][base_col+acc] == 'Q':
                        return False
            base_row, base_col = max(row+col-n+1, 0), min(row+col, n-1)
            for acc in range(0, base_col-base_row+1):
                if base_row+acc != row:
                    if chess[base_row+acc][base_col-acc] == 'Q':
                        return False
            return True
        
        def back_track(row):
            for col in range(n):
                if check_valid(row, col):
                    chess[row][col] = 'Q'
                    if row == n - 1:
                        chess_str = []
                        for i in range(n):
                            s = ''
                            for e in chess[i]:
                                s += e
                            chess_str.append(s)
                        res.append(chess_str)
                    else:
                        back_track(row+1)
                    chess[row][col] = '.'
            return
        
        back_track(0)
        return res