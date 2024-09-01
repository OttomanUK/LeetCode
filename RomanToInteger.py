class Solution(object):
    def romanToInt(self, s):
        result = 0
        found = []
        conversion = {
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000,
        }
        i = 0
        while i < len(s):
            if s[i:i+2]  in conversion and i+1<len(s):
                result = result + conversion[s[i:i+2]]
                i = i + 2
            else:
                result = result + conversion[s[i]]
                i = i + 1
        return result

    
solution = Solution()
solution.romanToInt("MCMXCIV")
