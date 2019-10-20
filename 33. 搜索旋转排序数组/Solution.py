class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []: return -1
        '''search for rotating point'''
        left = 0
        right  = len(nums) - 1
        if right == left:
            return right if nums[right] == target else -1
        while right - left > 1:
            p = (right + left) // 2
            if nums[p] > nums[left]:
                left = p
            elif nums[p] < nums[right]:
                right = p
        
        '''search for target'''
        if nums[0] <= target <= nums[left]:
            left, right = 0, left
        elif nums[right] <= target <= nums[len(nums)-1]:
            left, right = right, len(nums) - 1
        else:
            return -1
        print(left, right)
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        while right - left >= 0:
            p = (right + left) // 2
            if nums[p] < target:
                left = p + 1
            elif nums[p] > target:
                right = p - 1
            else:
                return p
        return -1