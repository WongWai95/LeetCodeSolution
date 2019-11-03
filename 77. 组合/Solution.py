class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        def find_combine(begin, end, count, res):
            if count == 0:
                ret.append(res[:])
            else:
                for i in range(begin, end-count+2):
                    find_combine(i+1, end, count-1, res+[i])
            return
        find_combine(1, n, k, [])
        return ret