class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while(n):
            count = count + ( n&1) 
            n>>=1
        return count