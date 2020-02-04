class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_dict = {}
        for e in nums:
            if e not in hash_dict:
                hash_dict[e] = 1
            else:
                hash_dict[e] += 1
                if hash_dict[e] == 3:
                    hash_dict.pop(e)
                
        for e in hash_dict:
            return e