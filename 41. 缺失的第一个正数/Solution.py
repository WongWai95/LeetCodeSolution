class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash_set = set()
        
        for e in nums:
            if e > 0:
                hash_set.add(e)
        
        for n in range(1, len(nums)+2):
            if not n in hash_set:
                return n