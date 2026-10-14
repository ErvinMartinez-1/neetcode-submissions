class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
                continue
            currProfit = prices[r] - prices[l]
            maxProfit = max(maxProfit, currProfit)
        
        return maxProfit