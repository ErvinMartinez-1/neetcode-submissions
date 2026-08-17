class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxE = max(piles)
        l, r = 1, maxE

        while l <= r:
            m = (l+r) // 2
            currK = m
            total = 0
            for pile in piles:
                total += math.ceil(pile / currK)
            if total <= h:
                minK = currK
                r = m - 1
            else:
                l = m + 1
        return minK
        
