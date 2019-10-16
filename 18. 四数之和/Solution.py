class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        
        nums.sort()
        result = []
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        
        for p1 in range(len(nums)):
            if p1 > 0 and nums[p1] == nums[p1-1]:
                continue
            for p2 in range(p1+1, len(nums)):
                if p2 > p1 + 1 and nums[p2] == nums[p2-1]:
                    continue
                for p3 in range(p2+1, len(nums)):
                    if p3 > p2 + 1 and nums[p3] == nums[p3-1]:
                        continue
                    if target - nums[p1] - nums[p2] - nums[p3] in hash_map \
                    and hash_map[target - nums[p1] - nums[p2] - nums[p3]] > p3:
                        result .append([nums[p1], nums[p2], nums[p3], target - nums[p1] - nums[p2] - nums[p3]])
                        
        return result