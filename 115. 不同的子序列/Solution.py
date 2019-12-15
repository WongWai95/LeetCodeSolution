class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if s == '': return int(t == '')
        if t == '': return 1
        dp = [[0 for _ in range(len(s))] for _ in range(len(t))]

        
        dp[0][0] = int(t[0] == s[0])
        for j in range(1, len(t)):
            dp[j][0] = 0
        for i in range(1, len(s)):
            dp[0][i] = dp[0][i-1] + int(t[0] == s[i])

        for j in range(1, len(t)):
            for i in range(1, len(s)):
                if t[j] == s[i]:
                    dp[j][i] = dp[j-1][i-1] + dp[j][i-1]
                else:
                    dp[j][i] = dp[j][i-1]
        return dp[-1][-1]