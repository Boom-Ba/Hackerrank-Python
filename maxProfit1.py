class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<1:
                return 0
        min_price =prices[0]
        max_profit =0
        for i in range(1,n):
            if prices[i] < min_price:
                min_price = prices[i]
            curr_profit = prices[i] -min_price
            if curr_profit > max_profit:
                max_profit = curr_profit
        return max_profit
            
                
            
        
                
            
        