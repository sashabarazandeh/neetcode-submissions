class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # start at day 1. small transactions alwys equal the real one, if its a negative ignoer, otherwise add to profit.
        profit = 0
        for i in range(1, len(prices)):
            calc = prices[i] - prices[i-1]
            if calc > 0:
                profit += calc
        return profit
            