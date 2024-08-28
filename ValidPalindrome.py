class Solution(object):
    def isPalindrome(self, s):
        newString = "".join(x for x in s if x.isalnum())
        newString = str.lower(newString)
        if newString == newString[::-1]:
            return True


solution = Solution()
result = solution.isPalindrome("A man, a plan, a canal: Panama")
print(result)
        