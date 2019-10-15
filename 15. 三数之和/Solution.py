class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        
        result = []
        hash_map = {}
        
        nums.sort()
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                if 0 - nums[i] - nums[j] in hash_map and hash_map[0 - nums[i] - nums[j]] > j:
                    result.append([nums[i], nums[j], 0 - nums[i] - nums[j]])
        return result