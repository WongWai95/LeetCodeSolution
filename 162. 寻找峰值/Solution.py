class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        # nums.append(-float('inf'))
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left + 1) // 2
            # if nums[mid-1] < nums[mid] < nums[mid+1]:
            #     return mid
            if nums[mid-1] < nums[mid]:
                left = mid
            elif nums[mid-1] > nums[mid]:
                right = mid - 1
        return left