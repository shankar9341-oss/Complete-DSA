class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_prices = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_prices = max(max_prices, profit)
            else:
                left = right
            right += 1
        return max_prices

        

