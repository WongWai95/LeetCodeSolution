class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def find_combine(ori: list, count: int, res: list) -> None:
            if count == 0:
                ret.append(res)
            else:
                for i in range(len(ori)-count+1):
                    find_combine(ori[i+1:], count-1, res+[ori[i]])
            return
        for i in range(0, len(nums)+1):
            find_combine(nums[:], i, [])
        return ret