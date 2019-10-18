class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []: return 0
        
        index = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[index] = nums[i]
                index += 1
        return index