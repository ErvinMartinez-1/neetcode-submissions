class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxA = 0
        while l < r:
            limit = min(heights[l], heights[r])
            width = r - l
            currArea = limit * width
            maxA = max(maxA, currArea)

            if limit == heights[l]:
                l += 1
            else:
                r -= 1
        return maxA