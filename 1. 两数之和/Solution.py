class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i
            
        for i in range(len(nums)):
            goal = target - nums[i]
            res = hash_map.get(goal) 
            if res!=None and res!=i:
                return [i, res]
        
        raise InterruptError