class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_n, one_n, two_n = 0, 0, 0
        for e in nums:
            if e == 0:
                zero_n += 1
            elif e == 1:
                one_n += 1
            else:
                two_n += 1
        for i in range(len(nums)):
            if zero_n:
                zero_n -= 1
                nums[i] = 0
            elif one_n:
                one_n -= 1
                nums[i] = 1
            else:
                two_n -= 1
                nums[i] = 2