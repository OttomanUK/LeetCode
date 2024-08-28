class Solution(object):
    def isPalindrome(self, x):
       x = str(x)
       xlist = []
       reversedX = []
       for letter in x:
           xlist.append(letter)
       for i in range(len(xlist)):
           reversedX.append(xlist[-(i+1)])
       if xlist == reversedX:
           return True
                   
           
solution = Solution()
result = solution.isPalindrome(121)
print(result)