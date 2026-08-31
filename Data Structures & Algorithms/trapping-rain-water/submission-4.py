class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL = maxR = 0
        total = 0
        while l < r:
            if height[l] < height[r]:
                curr = maxL - height[l]
                if curr < 0:
                    curr = 0
                maxL = max(maxL, height[l])
                total += curr
                l += 1
            else:
                curr = maxR - height[r]
                if curr < 0:
                    curr = 0
                maxR = max(maxR, height[r])
                total += curr
                r -= 1
        return total