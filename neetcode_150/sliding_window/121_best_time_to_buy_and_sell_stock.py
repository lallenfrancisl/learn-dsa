class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = 0
        sell = min(1, len(prices))
        max_profit = 0

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)

            sell += 1

        return max_profit
