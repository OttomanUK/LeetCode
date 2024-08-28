class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        result = [1] * length
        leftprod = 1
        for i in range(length):
            result[i] = leftprod
            leftprod = leftprod * nums[i]
        rightprod = 1 
        for i in range(length-1, -1, -1):
            result[i] = result[i]*rightprod
            rightprod = rightprod * nums[i]
        return result


        
solution = Solution()
result = solution.productExceptSelf([1,2,3,4])
print(result)
