class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []: return 0
        r_max = [0 for _ in range(len(prices))]
        r_max[-1] = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            r_max[i] = max(r_max[i+1], prices[i])

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, r_max[i]-prices[i])
        return max_profit