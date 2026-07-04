class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1 
        profit = 0 
        maxprofit = 0
        while left < right < len(prices) : 
            if prices[right] < prices[left]: 
                left = right 
            profit = prices[right] - prices[left]
            if profit > maxprofit : 
                 maxprofit = profit
            right +=1
            

        return maxprofit 

