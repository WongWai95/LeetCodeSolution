class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-2], dp[-1] = int(bool(int(s[-1]))), 1
        for i in range(len(s)-2, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1] if int(s[i:i+2]) > 26 else dp[i+1] + dp[i+2]
        return dp[0]