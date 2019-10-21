class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''check for row valid'''
        for i in range(len(board)):
            hash_set = set()
            for e in board[i]:
                if not e == '.':
                    if e in hash_set:
                        return False
                    else:
                        hash_set.add(e)

        '''check for column valid'''
        for col in range(len(board[0])):
            hash_set = set()
            for row in range(len(board)):
                if not board[row][col] == '.':
                    if board[row][col] in hash_set:
                        return False
                    else:
                        hash_set.add(board[row][col])

        '''check for sub_board valid'''
        for start_c, start_r in [(c, r) for c in [0, 3, 6] for r in [0, 3, 6]]:
            hash_set = set()
            for col in range(start_c, start_c+3):
                for row in range(start_r, start_r+3):
                    if not board[row][col] == '.':
                        if board[row][col] in hash_set:
                            return False
                        else:
                            hash_set.add(board[row][col])
        
        return True