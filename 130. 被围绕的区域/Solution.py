class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == None: return
        mask = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        def fill_closed(row: int, col: int) -> None:
            stack = [(row, col)]
            opened = []
            res = True
            while not stack == []:
                cur = stack.pop()
                mask[cur[0]][cur[1]] = True
                if cur[0] != 0 and board[cur[0]-1][cur[1]] == 'O' and mask[cur[0]-1][cur[1]] == False:
                    stack.append((cur[0]-1, cur[1]))
                if cur[0] != len(board)-1 and board[cur[0]+1][cur[1]] == 'O' and mask[cur[0]+1][cur[1]] == False:
                    stack.append((cur[0]+1, cur[1]))
                if cur[1] != 0 and board[cur[0]][cur[1]-1] == 'O' and mask[cur[0]][cur[1]-1] == False:
                    stack.append((cur[0], cur[1]-1))
                if cur[1] != len(board[0])-1 and board[cur[0]][cur[1]+1] == 'O' and mask[cur[0]][cur[1]+1] == False:
                    stack.append((cur[0], cur[1]+1))
                opened.append(cur)
                if cur[0] == 0 or cur[0] == len(board)-1 or cur[1] == 0 or cur[1] == len(board[0])-1:
                    res = False
            if res:
                while not opened == []:
                    cur = opened.pop()
                    board[cur[0]][cur[1]] = 'X'
            return
        for row in range(len(board)):
            for col in range(len(board[0])):
                if mask[row][col] == False and board[row][col] == 'O':
                    fill_closed(row, col)
        return