class Solution:
    def reverseBits(self, n):
        n = bin(n)[2:].zfill(32)
        reversedString = n[::-1]
        result = int(reversedString, 2)
        return result
        
solution = Solution()
result = solution.reverseBits(24)
print(result)
