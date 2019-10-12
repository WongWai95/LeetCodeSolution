class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list_merge = nums1 + nums2
        list_merge.sort()
        
        length = len(list_merge)
        if length%2==0:
            return (list_merge[length//2] + list_merge[length//2-1]) / 2
        else:
            return list_merge[length//2]