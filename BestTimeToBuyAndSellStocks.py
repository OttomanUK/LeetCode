class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        lowest = float('inf')
        for price in prices:
            if(lowest>price):
                lowest = price
            else:
                profit = price - lowest
                if (profit>maxProfit):
                    maxProfit = profit
        return maxProfit
    
solution = Solution()
result = solution.maxProfit([7,1,5,6,4])
print(result) 



