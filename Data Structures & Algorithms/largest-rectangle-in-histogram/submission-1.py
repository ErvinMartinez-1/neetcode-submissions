class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stck = []
        maxA = 0

        for i, h in enumerate(heights):
            begin = i
            while stck and h < stck[-1][1]:
                index, height = stck.pop()  
                area = (i - index) * height
                maxA = max(maxA, area)
                begin = index
            stck.append((begin, h))

        
        while stck:
            index, height = stck.pop()
            area = (len(heights) - index) * height
            maxA = max(maxA, area)
        
        return maxA

