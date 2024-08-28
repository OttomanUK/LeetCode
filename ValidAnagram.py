from collections import Counter


#Unoptimized
class Solution(object):
    def isAnagram(self, s, t):
        sLength = len(s)
        tLength = len(t)
        foundIndexes = []
        for i in range(sLength):
            for j in range(tLength):
                if j not in foundIndexes and s[i] == t[j]:
                    foundIndexes.append(j)
                    break
        if len(foundIndexes) != sLength or len(foundIndexes)!= tLength:
            return False
        return True


#Optimized Using Counter
class CounterSolution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
    

#Optimized Without Counter    
class OptimizedSolution(object):
    def isAnagram(self,s,t):
        sObj = {}
        tObj = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in sObj:
                sObj[i] = 1
            else:
                sObj[i] = sObj[i] + 1
        for j in t:
            if j not in tObj:
                tObj[j] = 1
            else:
                tObj[j] = tObj[j] + 1
        return sObj == tObj

        


solution = OptimizedSolution()
result = solution.isAnagram('cat','rat')
print(result)