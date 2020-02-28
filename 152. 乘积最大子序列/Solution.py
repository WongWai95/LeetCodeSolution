class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        from functools import reduce
        def sub_func(begin, end):
            if begin >= end:
                return 0
            positive = True
            multiple_func = lambda x, y: x*y
            for e in nums[begin:end]:
                if e < 0:
                    positive = not positive
            if positive:
                return reduce(multiple_func, nums[begin:end], 1)
            else:
                max_sub_mul = nums[begin]
                left_neg = right_neg = begin
                for i in range(begin, end):
                    if nums[i] < 0:
                        left_neg = i
                        break
                for i in range(end-1, begin-1, -1):
                    if nums[i] < 0:
                        right_neg = i 
                        break
                
                return max(
                    max_sub_mul,
                    reduce(multiple_func, nums[left_neg+1: end], 1) if left_neg+1 < end else -float('inf'),
                    reduce(multiple_func, nums[begin: right_neg], 1) if begin < right_neg else -float('inf')
                )
        max_multiple = nums[0]
        zero_begin = 0
        for split in range(len(nums)):
            if nums[split] == 0:
                # print('zero: ', split, '\nenter: ', zero_begin, split)
                # print('sub_result: ', sub_func(zero_begin, split))
                max_multiple = max(max_multiple, 0, sub_func(zero_begin, split))
                zero_begin = split + 1
        return max(max_multiple, sub_func(zero_begin, len(nums)))