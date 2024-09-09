class Solution(object):
    def construct2DArray(self, original, m, n):
        result = []
        row = []
        length = len(original)
        if length != m * n:
            return []
        for i, element in enumerate(original):
            row.append(element)
            if (i+1)%n==0:
                result.append(row)
                row = []
        return result


solution = Solution()
result = solution.construct2DArray([1,2,3,4],2,2)
print(result)


