class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        heights = [0] + heights + [0]
        max_area = 0
        for i in range(1, len(heights)):
            while heights[i] < heights[stack[-1]]:
                tmp = stack.pop()
                max_area = max(max_area, heights[tmp]*(i-stack[-1]-1))
            stack.append(i)
        return max_area