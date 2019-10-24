class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        po = 1
        if n < 0:
            x = 1 / x
            n = -n

        import math
        res = x
        hash_map = {0: 1, 1:x}
        while po * 2 <= n:
            res = res ** 2
            po *= 2
            hash_map[po] = res
        n = n - po
        while n > 0:
            po = 2 ** int(math.log(n, 2))
            res *= hash_map[po]
            n -= po
        return res