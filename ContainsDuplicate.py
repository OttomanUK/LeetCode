class Solution(object):
    def containsDuplicate(self, nums):
        present = set()
        for i in nums:
            if i in present:
                return True
            present.add(i)

                    
       
    
solution = Solution()
result = solution.containsDuplicate([1,2,1,4])
print(result)



class pracSol(object):
    def containsDuplicate(self, nums):
        present = set()
        for num in nums:
            if num in present:
                return True
            else:
                present.add(num)
