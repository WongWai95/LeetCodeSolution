class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def iteration(remain: List[int], result: List[int], n: int) -> None:
            if n == 0: res.append([])
            elif n == 1:
                res.append(result+[remain[0]])
                last_num = remain[0]
                for i in range(1, len(remain)):
                    if remain[i] != last_num:
                        res.append(result+[remain[i]])
                    last_num = remain[i]
            else:
                last_num = remain[0]
                iteration(remain[1:], result+[remain[0]], n-1)
                for i in range(1, len(remain)-n+1):
                    if remain[i] != last_num:
                        iteration(remain[i+1:], result+[remain[i]], n-1)
                    last_num = remain[i]
        nums.sort()
        if nums == []: return []
        for i in range(len(nums)+1):
            iteration(nums, [], i)
        return res