class Solution(object):
    def lengthOfLastWord(self, s):
        arr = s.split()
        length = len(arr)
        word = arr[length-1]
        return word
    

solution = Solution()
result = solution.lengthOfLastWord("Hello World")
print(result)