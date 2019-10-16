class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        
        for left in range(0, len(nums)-2):
            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                if abs(nums[left] + nums[middle] + nums[right] - target) < abs(closest - target):
                    closest = nums[left] + nums[middle] + nums[right]
                if nums[left] + nums[middle] + nums[right] < target:
                    middle += 1
                elif nums[left] + nums[middle] + nums[right] > target:
                    right -= 1
                else:
                    return nums[left] + nums[middle] + nums[right]
                    
        return closest