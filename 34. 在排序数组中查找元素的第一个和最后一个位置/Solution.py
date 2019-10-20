class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''search for one of the targets'''
        left, mid, right = 0, -1, len(nums) - 1
        while right >= left:
            p = (left + right) // 2
            if nums[p] < target:
                left = p + 1
            elif nums[p] > target:
                right = p - 1
            else:
                mid = p
                break
        if mid == -1:
            return [-1, -1]
        print(left, mid, right)
        
        '''search for left bound'''
        l, r = left, mid
        while r - l > 0:
            p = (l + r) // 2
            if nums[p] == target:
                r = p
            else:
                l = p + 1
        l_bound = r
        
        '''search for right bound'''
        l, r = mid, right
        while r - l > 0:
            p = (l + r + 1) // 2
            if nums[p] == target:
                l = p
            else:
                r = p - 1
        r_bound = l
        
        return [l_bound, r_bound]