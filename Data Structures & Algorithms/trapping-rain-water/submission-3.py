class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = maxR = totalA = l = 0
        r = len(height) - 1

        while l <= r:
            if maxL < maxR:
                area = maxL - height[l]
                if area < 0:
                    area = 0
                totalA += area
                maxL = max(maxL, height[l])
                l += 1
            else:
                area = maxR - height[r]
                if area < 0:
                    area = 0
                totalA += area
                maxR = max(maxR, height[r])
                r -= 1      

        return totalA        

                


                
