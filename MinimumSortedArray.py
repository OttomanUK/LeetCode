class Solution(object):
    def findMin(self, nums):
        length = len(nums)
        left = 0
        right = length - 1

        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = left + (right - left) // 2
            if mid > 0 and nums[mid] < nums[mid] - 1:
                return mid
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        return nums[left]
            

solution = Solution()
result = solution.findMin([3,4,5,1,2])
print(result)
