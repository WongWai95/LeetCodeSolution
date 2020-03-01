class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        min_num = nums[left]
        if nums[left] == nums[right]:
            for e in nums:
                min_num = min(min_num, e)
            return min_num

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[right]:
                right = mid
            elif nums[mid] >=nums[left]:
                left = mid + 1
        return nums[left]