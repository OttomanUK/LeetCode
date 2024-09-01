class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        length = len(nums)
        for i in range(length-2):
            left = i + 1
            right = length - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left = left + 1
                elif total > 0:
                    right = right - 1 
                else:
                    temp = [nums[i], nums[left], nums[right]]
                    if temp not in result:
                        result.append(temp)
                    while left < right and nums[left] == nums[left] + 1:
                        left = left + 1
                    while left < right and nums[right] == nums[right] - 1:
                        right = right - 1
                    left = left + 1
                    right = right - 1
        return result
    

solution = Solution()
result = solution.threeSum([-2,0,0,2,2])
print(result)
                
