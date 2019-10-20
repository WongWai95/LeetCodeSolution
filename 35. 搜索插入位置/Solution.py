class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums == []: return 0
        left, right = 0, len(nums) - 1
        while left < right:
            p = (left + right) // 2
            if nums[p] < target:
                left = p + 1
            else:
                right = p
        return right+1 if right == len(nums) - 1 and target > nums[right] else right