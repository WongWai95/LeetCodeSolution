class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        step, step_index = 0, 0
        left, right = 0, 0
        
        while left < len(nums) - 1:
            step = 0
            for right in range(left+1, left+1+nums[left]):
                if right == len(nums) - 1:
                    count += 1
                    return count
                if step <= nums[right] - nums[left] + right - left:
                    step = nums[right] - nums[left] + right - left
                    step_index = right
            left = step_index
            count += 1
        
        return count