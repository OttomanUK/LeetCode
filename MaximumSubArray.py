class Solution:
    def maxSubArray(self, nums):       
        result = nums[0]
        total = 0
        for num in nums:
            if total < 0:
                total = 0
            total = total + num
            result = max(result, total)
        return result
    
solution = Solution()
result = solution.maxSubArray([5,4,-1,7,8])
print(result)