class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for row in range(length//2):
            for col in range(row, length-row-1):
                # matrix[row][col], matrix[col][length-1-row], matrix[length-1-row][length-1-col], matrix[length-1-col][row]
                matrix[col][length-1-row], matrix[length-1-row][length-1-col], matrix[length-1-col][row], matrix[row][col] = matrix[row][col], matrix[col][length-1-row], matrix[length-1-row][length-1-col], matrix[length-1-col][row]
        return