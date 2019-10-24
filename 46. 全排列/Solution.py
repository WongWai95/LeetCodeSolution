class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        def get_next() -> bool:
            p = -1
            for i in range(length-1, 0, -1):
                if nums[i] > nums[i-1]:
                    p = i
                    break
            if p == -1:
                return False
            
            k = -1
            for i in range(length-1, p-1, -1):
                if nums[i] > nums[p-1]:
                    k = i
                    break
            nums[p-1], nums[k] = nums[k], nums[p-1]
            for i in range(p, (p+length+1)//2):
                nums[i], nums[length-i+p-1] = nums[length-i+p-1], nums[i]
            return True
        
        res = [nums[:]]
        while get_next() == True:
            res.append(nums[:])
        return res