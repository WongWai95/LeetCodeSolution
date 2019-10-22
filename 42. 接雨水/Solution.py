class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0 for _ in range(len(height))]
        left_max = 0
        for i in range(len(height)):
            left[i] = max(left_max, height[i])
            left_max = max(left_max, height[i])
        print(left)
        right = [0 for _ in range(len(height))]
        right_max = 0
        for i in range(len(height)-1, -1, -1):
            right[i] = max(right_max, height[i])
            right_max = max(right_max, height[i])
        print(right)
        res = 0
        for i in range(len(height)):
            res += min(left[i], right[i]) - height[i]
        return res