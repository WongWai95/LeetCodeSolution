class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if nums == []: return 
        first_index = second_index = None
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                first_index = i
                break
        if first_index == None:
            for i in range((len(nums)+1)//2):
                nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
            return
        for i in range(len(nums)-1, first_index-1, -1):
            if nums[i] > nums[first_index]:
                second_index = i
                break
        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
        for i in range(first_index+1, (len(nums)-first_index)//2+first_index+1):
                nums[i], nums[len(nums)-i+first_index] = nums[len(nums)-i+first_index], nums[i]
        return