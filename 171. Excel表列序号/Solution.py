class Solution:
    def titleToNumber(self, s: str) -> int:
        base = 1
        res = 0
        while len(s) != 0:
            bias = ord(s[-1]) - ord('A') + 1
            res += bias * base

            s = s[:-1]
            base *= 26

        return res