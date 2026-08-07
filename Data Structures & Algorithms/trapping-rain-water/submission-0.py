class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR, totalWater = 0, 0, 0

        while l <= r:
            if maxL < maxR:
                total = maxL - height[l]
                if total < 0:
                    total = 0 
                totalWater += total
                maxL = max(maxL, height[l])
                l += 1
            else:
                total = maxR - height[r]
                if total < 0:
                    total = 0 
                totalWater += total
                maxR = max(maxR, height[r])
                r -= 1

        return totalWater

                


                
