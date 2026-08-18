class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxA = 0

        while l < r:
            limiter = min(heights[l], heights[r])
            width = r - l
            area = width * limiter
            maxA = max(maxA, area)
            if limiter == heights[l]:
                l += 1
            else:
                r -= 1
        
        return maxA
