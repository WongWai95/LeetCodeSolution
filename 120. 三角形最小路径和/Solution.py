class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle == []: return 0
        dp = triangle[:][:]
        for row in range(1, len(triangle)):
            dp[row][0] = triangle[row][0] + dp[row-1][0]
            for col in range(1, len(triangle[row])-1):
                dp[row][col] = min(dp[row-1][col-1], dp[row-1][col]) + triangle[row][col]
            dp[row][-1] = triangle[row][-1] + dp[row-1][-1]
        return min(dp[-1])