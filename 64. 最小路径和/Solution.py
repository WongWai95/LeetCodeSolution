class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid == []: return 0
        row_n, col_n = len(grid), len(grid[0])
        dp = [[None for _ in range(col_n)] for _ in range(row_n)]
        
        dp[-1][-1] = grid[-1][-1]
        for i in range(row_n-2, -1, -1):
            dp[i][-1] = dp[i+1][-1] + grid[i][-1]
        for i in range(col_n-2, -1, -1):
            dp[-1][i] = dp[-1][i+1] + grid[-1][i]
            
        for col in range(col_n-2, -1, -1):
            for row in range(row_n-2, -1, -1):
                dp[row][col] = grid[row][col] + min(dp[row+1][col], dp[row][col+1])
        return dp[0][0]