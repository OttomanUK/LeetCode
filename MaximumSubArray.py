class Solution(object):
    def maxSubArray(self, nums):
        result = nums[0]
        total = 0
        for num in nums:
            if total < 0:
                total = 0
            total = total + num
            result = max(result, total)
        return result 
    
