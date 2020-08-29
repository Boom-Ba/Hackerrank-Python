class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<1:
                return 0
        min_price =[0]*n
        max_price=[0]*n
        min_price[0] =prices[0] #7
        max_price[0] = 0
        for i in range(1,n):
            min_price[i] =min(min_price[i-1], prices[i])
            max_price[i] = max((prices[i] - min_price[i-1]), max_price[i-1])
        return max_price[n-1]
            
                
            
        