#Unoptimized Solution
class Solution(object):
    def missingNumber(self, nums):
        length = len(nums)
        for i in range(length+1):
            if i not in nums:
                return i

# solution = Solution()
# result = solution.missingNumber([0,1,3])
# print(result)


#Optimized Solution
class OptimizedSolution(object):
    def missingNumber(self,nums):
        numSet = set(nums)
        for i in range(len(numSet)+1):
            if i not in numSet:
                return i
        
      
        

solution = OptimizedSolution()
result = solution.missingNumber([0,1,3])
print(result)