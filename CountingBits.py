class Solution(object):
    def hammingWeight(self,n):
        count = 0
        while(n):
            count = count + (n & 1)
            n >>= 1
        return count

        
    def countBits(self, n):
        arr = [0]  * (n+1)
        for i in range(len(arr)):
            arr[i] = self.hammingWeight(i)
        print(arr)
       
      


solution = Solution()
solution.countBits(5)