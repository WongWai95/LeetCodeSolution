class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[None for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][0] = True
        for i in range(len(s)-1):
            dp[i][1] = s[i]==s[i+1]
        for step in range(2, len(s)):
            for begin in range(len(s)-step):
                dp[begin][step] = dp[begin+1][step-2] and s[begin]==s[begin+step]
        
        res = []
        def iteration(begin: int, path: list):
            if begin == len(s):
                res.append(path)
            for step in range(len(s)-begin):
                if dp[begin][step] == True:
                    iteration(begin+step+1, path+[s[begin:begin+step+1]])
        iteration(0, [])
        return res