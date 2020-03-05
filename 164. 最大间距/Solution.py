class Bucket:
    def __init__(self):
        self.used = False
        self.max_val = -float('inf')
        self.min_val = float('inf')

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        maxi = max(nums)
        mini = min(nums)
        length = len(nums)

        bucket_size = max(1, (maxi - mini) // (length - 1))
        bucket_num = (maxi - mini) // bucket_size + 1
        bucket = [Bucket() for _ in range(bucket_num)]
        for e in nums:
            bucket_index = (e - mini) // bucket_size
            bucket[bucket_index].used = True
            bucket[bucket_index].max_val = max(bucket[bucket_index].max_val, e)
            bucket[bucket_index].min_val = min(bucket[bucket_index].min_val, e)

        max_gap = -1
        last_max = mini 
        for b in bucket:
            if b.used:
                max_gap = max(max_gap, b.min_val - last_max)
                last_max = b.max_val
        
        return max_gap