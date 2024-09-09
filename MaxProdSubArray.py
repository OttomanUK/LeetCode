class Solution(object):
       def maxProduct(self, nums):
        max_prod = min_prod = result = nums[0]
        for num in nums[1:]:
            if num < 0:
                # Swap max_prod and min_prod when the current number is negative
                max_prod, min_prod = min_prod, max_prod
            
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            
            result = max(result, max_prod)
        
        return result