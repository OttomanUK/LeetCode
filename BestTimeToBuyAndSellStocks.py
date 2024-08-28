# class Solution(object):
#     def maxProfit(self, prices):
#         maxProfit = 0
#         lowest = float('inf')
#         for price in prices:
#             if(lowest>price):
#                 lowest = price
#             else:
#                 profit = price - lowest
#                 if (profit>maxProfit):
#                     maxProfit = profit
#         return maxProfit
    
# solution = Solution()
# result = solution.maxProfit([7,1,5,6,4])
# print(result) 


class Solution(object):
    def maxProfit(self,prices):
        maxprofit = 0
        length = len(prices)
        for i in range(length-1):
            for j in range(i+1, length):
                profit = prices[j] - prices[i]
                if prices[i]<prices[j] and maxprofit<=profit:
                    profit = prices[j] - prices [i]
                    maxprofit = profit
        print(maxprofit)

solution = Solution()
solution.maxProfit([7,1,5,6,4])
