class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                temp = temp + prices[i] - prices[i-1]
        return temp