class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def iteration(remain: str, n: int, result: str) -> None:
            if n == 0 and remain == '':
                res.append(result[1:])
                return
            if remain == '':
                return
            if remain[0] == '0': 
                iteration(remain[1:], n-1, result+'.'+remain[:1])
                return
            for i in range(1, min(3, len(remain))+1):
                if int(n == 4) <= int(remain[:i]) <= 255:
                    iteration(remain[i:], n-1, result+'.'+remain[:i])
        if len(s) > 16: return res
        iteration(s, 4, '')
        return res