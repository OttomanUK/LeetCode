class Solution(object):
    def function(self,arr, target):
        count = 0
        for row in arr:
            if row == target:
                count = count + 1
        return count

solution = Solution()
twoDArray = [[2,3,4], [2,3,4], [2,3,4]]
result = solution.function( twoDArray,[2,3,4])
print(result)