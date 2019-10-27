class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def get_subperm(l: list, num: int) -> list:
            if num == 1: return l
            def calc_n(x):
                if x == 1: return 1
                return x * calc_n(x - 1)
            per_group = calc_n(len(l)-1)
            head = l[(num - 1 ) // per_group]
            order = ((num - 1 ) // per_group + 1) * per_group - per_group + 1
            l.pop((num - 1 ) // per_group)
            return [head] + get_subperm(l[:], num-order+1)
        res_list = get_subperm([i for i in range(1, n+1)], k)
        res = ''
        for e in res_list:
            res += str(e)
        return res