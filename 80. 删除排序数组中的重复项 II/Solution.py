class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []: return 0
        left = 1
        last_num = nums[0]
        count = 1
        for right in range(1, len(nums)):
            if nums[right] == last_num:
                count += 1
            else:
                last_num = nums[right]
                count = 1
            if count <= 2:
                nums[left] = nums[right]
                left += 1
        return left