class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stck = []
        maxA = 0

        for i, h in enumerate(heights):
            curr = i
            if not stck:
                stck.append([i, h])
                continue
            while stck and h < stck[-1][1]:
                index, height = stck.pop()
                area = (i - index) * height
                maxA = max(maxA, area)
                curr = index
            stck.append([curr, h])

        while stck:
            index, height = stck.pop()
            area = (len(heights) - index) * height
            maxA = max(maxA, area)

        return maxA