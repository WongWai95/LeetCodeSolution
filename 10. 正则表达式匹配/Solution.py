class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '':
            return not s
        
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (bool(s) and p[0] in [s[0], '.'] and self.isMatch(s[1:], p))
        
        return bool(s) and p[0] in [s[0], '.'] and self.isMatch(s[1:], p[1:])