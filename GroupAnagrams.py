class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        result = []
        for word in strs:
            sortedWord = "".join((sorted(word)))
            if sortedWord not in anagrams:
                anagrams[sortedWord] = []
            anagrams[sortedWord].append(word)
        for value in anagrams.values():
            result.append(value)
        return result


solution = Solution()
result = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)
