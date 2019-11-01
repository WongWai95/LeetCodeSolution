class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return matrix
        row_mem = [False for _ in range(len(matrix))]
        col_mem = [False for _ in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    row_mem[row] = True
                    col_mem[col] = True
        for row in range(len(row_mem)):
            if row_mem[row] == True:
                for col in range(len(matrix[0])):
                    matrix[row][col] = 0
        for col in range(len(col_mem)):
            if col_mem[col] == True:
                for row in range(len(matrix)):
                    matrix[row][col] = 0