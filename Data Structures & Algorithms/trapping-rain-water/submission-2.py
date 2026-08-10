class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR, maxArea = 0, 0, 0
        l, r = 0, len(height) - 1

        while l <= r:
            if maxL < maxR:
                currArea = maxL - height[l]
                if currArea < 0:
                    currArea = 0
                maxArea += currArea
                maxL = max(maxL, height[l])
                l += 1
            else:
                currArea = maxR - height[r]
                if currArea < 0:
                    currArea = 0
                maxArea += currArea
                maxR = max(maxR, height[r])
                r -= 1   

        return maxArea             