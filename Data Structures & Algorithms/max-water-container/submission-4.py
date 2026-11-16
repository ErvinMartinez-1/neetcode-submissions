class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        while l != r:
            width = r - l
            length = min(heights[l], heights[r])
            area = width * length
            maxArea = max(maxArea, area)
            if length == heights[l]:
                l += 1
            else:
                r -= 1
        return maxArea