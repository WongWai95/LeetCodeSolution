class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        
        row_n = 0
        left, right = 0, len(matrix)-1
        while left < right:
            mid = (right + left + 1) // 2
            if matrix[mid][0] <= target:
                left = mid
            else:
                right = mid - 1
        if matrix[left][0] > target:
            return False
        row_n = left

        left, right = 0, len(matrix[0])-1
        while left <= right:
            mid = (right + left) // 2
            if matrix[row_n][mid] == target:
                return True
            elif matrix[row_n][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False