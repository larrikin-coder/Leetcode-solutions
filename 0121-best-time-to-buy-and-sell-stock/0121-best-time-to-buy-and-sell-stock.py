class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in prices[1:]:
            max_profit = max(max_profit,i - min_price)
            min_price = min(i,min_price)
        return max_profit


