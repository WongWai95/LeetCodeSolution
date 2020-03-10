class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        critic = length // 2
        hash_map = {}
        for e in nums:
            if e in hash_map:
                hash_map[e] += 1
            else:
                hash_map[e] = 1
            
            if hash_map[e] > critic:
                return e 
        return None