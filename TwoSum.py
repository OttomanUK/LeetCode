class Solution(object):
    def twoSum(self, nums, target):
        output = []
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1,length):
                if nums[i]+nums[j] == target:
                    output.append(i)
                    output.append(j)
        return output
    
solution = Solution()
result = solution.twoSum([2,3,4],5)
print(result)



