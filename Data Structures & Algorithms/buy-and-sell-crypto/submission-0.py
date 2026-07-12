class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low_price = 0
        best_res = 0

        for i in range(len(prices)): 
            # first check : pre state 
            # calculate profit: 
            if (i == 0): 
                low_price = prices[i]
            profit = prices[i] - low_price

            if (prices[i] < low_price): 
                low_price = prices[i]    
            if ( profit > best_res) : 
                best_res = profit

        return best_res