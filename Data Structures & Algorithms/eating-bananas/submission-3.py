class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = 0
        while l <= r:
            k = (l+r) // 2
            numHours = 0

            for pile in piles:
                numHours += math.ceil(pile / k)

            if numHours <= h:
                minK = k
                r = k - 1
            else:
                l = k + 1
        return minK

