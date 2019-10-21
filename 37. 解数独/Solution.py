class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''check if one step is valid'''
        def check_valid(row: int, col: int, num: int) -> bool:
            hash_row = set()
            hash_col = set()
            hash_sub = set()
            '''build hashset for row'''
            for e in board[row]:
                if not e == '.':
                    hash_row.add(e)
            '''build hashset for column'''
            for i in range(len(board[0])):
                if not board[i][col] == '.':
                    hash_col.add(board[i][col])
            '''build hashset for sub-board'''
            start_r, start_c = row // 3 * 3, col // 3 * 3
            for r, c in [(r, c) for r in range(start_r, start_r+3) for c in range(start_c, start_c+3)]:
                if not board[r][c] == '.':
                    hash_sub.add(board[r][c])
            '''check validation'''
            return bool(not num in hash_row and not num in hash_col and not num in hash_sub)
        
        '''get next blank'''
        def get_next(row: int, col: int) -> (int, int):
            for c in range(col+1, len(board[0])):
                if board[row][c] == '.':
                    return (row, c)
            for r in range(row+1, len(board)):
                for c in range(len(board[0])):
                    if board[r][c] == '.':
                        return (r, c)
            return None
        '''initialization'''
        pool_stack = []
        current_status = (0, -1)
        first_blank = get_next(0, -1)
        pool_stack.append((first_blank[0], first_blank[1], '.'))
        for n in range(1, 10):
            if check_valid(first_blank[0], first_blank[1], str(n)) == True:
                pool_stack.append((first_blank[0], first_blank[1], str(n)))
        '''DFS algorithm'''
        while not pool_stack == []:
            # print(pool_stack)   # for debugging
            current_status = pool_stack[-1]
            pool_stack.pop()
            board[current_status[0]][current_status[1]] = current_status[2]
            if current_status[2] == '.': continue
            next_pos = get_next(current_status[0], current_status[1])
            if not next_pos == None:
                pool_stack.append((next_pos[0], next_pos[1], '.'))
                for n in range(1, 10):
                    if check_valid(next_pos[0], next_pos[1], str(n)) == True:
                        pool_stack.append((next_pos[0], next_pos[1], str(n)))
            else:
                return