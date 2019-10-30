class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid == []: return 0
        row_n, col_n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[None for _ in range(col_n)] for _ in range(row_n)]
        
        for i in range(row_n-1, -1, -1):
            if obstacleGrid[i][-1] == 0:
                dp[i][-1] = 1
            else:
                for j in range(i+1):
                    dp[j][-1] = 0
                break
        for i in range(col_n-1, -1, -1):
            if obstacleGrid[-1][i] == 0:
                dp[-1][i] = 1
            else:
                for j in range(i+1):
                    dp[-1][j] = 0
                break
        for row in range(row_n-2, -1, -1):
            for col in range(col_n-2, -1, -1):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row+1][col] + dp[row][col+1]
        return dp[0][0]