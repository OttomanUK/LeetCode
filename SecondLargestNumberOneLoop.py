class Solution(object):
    def secondLargest(self, arr):
        if len(arr)<2:
            return False
        largest = secondLargest = 0
        for num in arr:
            if num > largest:
                secondLargest = largest
                largest = num
            elif num > secondLargest and num != largest:
                secondLargest = num
        return secondLargest
    
    def secondSmallest(self, arr):
        smallest = secondSmallest = 10000
        if len(arr) < 2:
            return False
        for num in arr:
            if num < smallest:
                secondSmallest = smallest
                smallest = num
            elif num < secondSmallest and num!=smallest:
                secondSmallest = num
        return secondSmallest
    
solution = Solution()
result1 = solution.secondLargest([2,3,4,5,6])
result2 = solution.secondSmallest([2,3,4,5,6])
print(result1)
print(result2)
