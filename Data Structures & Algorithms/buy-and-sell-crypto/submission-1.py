class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minim = prices[0]

        for price in prices:
            ans = max(ans, price-minim)
            minim = min(minim, price)
        
        return ans