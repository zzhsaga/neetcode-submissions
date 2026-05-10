class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = math.inf
        for p in prices:
            l = min(p,l)
            profit = max(p-l,profit)
        
        return profit
