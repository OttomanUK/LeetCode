class Solution(object):
    def currencyDenomination(self, arr, target):
        j = len(arr) - 1
        result = []
        count = 0
        remaining = target
        while(remaining != 0 ):
            if arr[j] <= remaining:
                count = count + 1
                remaining = remaining - arr[j]
                result.append(arr[j])
            else:
                j = j - 1
        if (remaining == target):
            return False
        return count, result
    
solution = Solution()
result, arr = solution.currencyDenomination([10,20,50,500], 880)
print(result)
print(arr)