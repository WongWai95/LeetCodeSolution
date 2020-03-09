class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n > 0:
            n -= 1
            remainder = n % 26
            n = n // 26
            res = chr(ord('A') + remainder) + res
        return res