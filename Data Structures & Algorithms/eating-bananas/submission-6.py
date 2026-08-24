class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        l, r = 1, maxPile
        k = 0

        while l <= r:
            m = (l+r) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / m)

            if time > h:
                l = m + 1
            else:
                k = m
                r = m - 1
        return k
            



