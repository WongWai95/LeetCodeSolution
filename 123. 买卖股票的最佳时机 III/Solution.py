class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []: return 0
        s1 = -prices[0]
        s2 = s3 = s4 = -float('inf')
        
        for i in range(len(prices)):
            s1 = max(s1, -prices[i])
            s2 = max(s2, s1+prices[i])
            s3 = max(s3, s2-prices[i])
            s4 = max(s4, s3+prices[i])
            
        return max(0,s4)