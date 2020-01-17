class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_set = set()
        for e in nums:
            if e in hash_set:
                hash_set.remove(e)
            else:
                hash_set.add(e)
        for e in hash_set:
            return e