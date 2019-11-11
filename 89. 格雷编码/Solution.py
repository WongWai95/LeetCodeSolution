class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [0]
        res = [0]
        for index in range(1, n+1):
            len_res = len(res)
            for i in range(len_res-1, -1, -1):
                res.append(res[i]+2**(index-1))
        return res