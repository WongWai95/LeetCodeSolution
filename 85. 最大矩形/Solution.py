class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        row_len, col_len = len(matrix), len(matrix[0])
        histo = [0] * col_len
        max_area = 0
        for row in range(row_len):
            for col in range(col_len):
                histo[col] = histo[col] + 1 if matrix[row][col] == '1' else 0
            tmp_histo = [0] + histo + [0]
            stack = [0]
            for i in range(1, len(tmp_histo)):
                while tmp_histo[i] < tmp_histo[stack[-1]]:
                    tmp = stack.pop()
                    max_area = max(max_area, tmp_histo[tmp] * (i - stack[-1] - 1))
                stack.append(i)
        return max_area