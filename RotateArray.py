from copy import deepcopy

#unoptimized solution
class UnoptimizedSolution(object):
    def rotate(self, nums, k):
        length = len(nums)
        copyArr = deepcopy(nums)
        for i in range(length):
            pos = i+k
            if(pos<length):
                val = copyArr[i]
                pos = i+k
                nums[pos] = val
            else:
                index = pos % length
                val = copyArr[i]
                nums[index] = val
            print(nums)

#optimized solution
class Solution(object):
    def rotate(self,nums, k):
        length = len(nums)
        mod = k % length
        if mod == 0:
            return
        copyArr = nums[-mod:]
        for i in range(length-mod-1,-1,-1):
            nums[i+k] = nums[i]
        for k in range(len(copyArr)):
            nums[k] = copyArr[k]
        return nums

solution = Solution()
result = solution.rotate([3,2,4],2)
print(result)
