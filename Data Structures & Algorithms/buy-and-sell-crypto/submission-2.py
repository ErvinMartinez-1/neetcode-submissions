class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        maxProfit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
                continue
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
            r += 1
        
        return maxProfit