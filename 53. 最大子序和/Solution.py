class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        summ = 0
        
        for e in nums:
            if summ > 0:
                summ += e
            else:
                summ = e
            res = max(res, summ)
        return res