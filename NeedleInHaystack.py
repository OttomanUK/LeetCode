class Solution(object):
    def strStr(self, haystack, needle):
        length = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+length] == needle:
                return i
        return -1
    

solution = Solution()
result = solution.strStr("notsadsad","sad")
print(result)
