class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_p = 0
        right_p = len(height) - 1
        max_volume = 0
        while left_p < right_p:
            max_volume = max(max_volume, min(height[left_p], height[right_p]) * (right_p - left_p))
            if height[left_p] < height[right_p]:
                left_p += 1
            else:
                right_p -= 1
        
        return max_volume