class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        
        for i in range(len(word1)+1):
            dp[0][i] = i
        for i in range(len(word2)+1):
            dp[i][0] = i
        for i1 in range(1, len(word1)+1):
            for i2 in range(1, len(word2)+1):
                if word1[i1-1] == word2[i2-1]:
                    dp[i2][i1] = dp[i2-1][i1-1]
                else:
                    dp[i2][i1] = min(dp[i2-1][i1-1], dp[i2][i1-1], dp[i2-1][i1]) + 1
        return dp[-1][-1]