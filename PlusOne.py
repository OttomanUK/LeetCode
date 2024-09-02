class Solution(object):
    def plusOne(self, digits):
        stringInteger = ''.join(map(str,digits))
        integer = int(stringInteger) + 1
        result = str(integer)
        return list(result)


solution = Solution()
result = solution.plusOne([1,2,3])
print(result)
