class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = math.inf
        for p in prices:
            profit = max(p-l,profit)
            l = min(p,l)
            
        
        return profit
