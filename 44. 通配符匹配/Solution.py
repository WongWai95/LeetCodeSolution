class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        f = [[None for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        
        f[0][0] = True
        for i in range(1, len(p)+1):
            f[0][i] = f[0][i-1] and p[i-1] == '*'
        for i in range(1, len(s)+1):
            f[i][0] = False
            
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] != '*':
                    f[i][j] = f[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    f[i][j] = f[i-1][j] or f[i][j-1]
        
        return f[len(s)][len(p)]