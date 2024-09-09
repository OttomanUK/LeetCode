class Solution(object):
    def isPalindrome(self, word):
        newWord = ""
        for i in range(len(word)-1, -1, -1):
            newWord = newWord + word[i]
        if newWord == word:
            return True

solution = Solution()
result = solution.isPalindrome("hello")
print(result)

            
