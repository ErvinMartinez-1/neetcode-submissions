class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxVol = 0
        while l <= r:
            minBar = min(heights[l], heights[r])
            currentVol = minBar * (r - l)
            if currentVol > maxVol:
                maxVol = currentVol
            if minBar == heights[l]:
                l = l + 1
            if minBar == heights[r]:
                r = r - 1

        return maxVol