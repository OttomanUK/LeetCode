class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count = maxCount = 0 
        result = []
        for i, letter in enumerate(s):
            if letter not in result:
                result.append(letter)
                count = len(result)
                maxCount = max(maxCount, count)
            elif letter in result:
                index = result.index(letter)
                result = result[index+1:]
                result.append(letter)
        return maxCount

solution = Solution()
result = solution.lengthOfLongestSubstring("dvdf")
print(result)