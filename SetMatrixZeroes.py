class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        rowArr = []
        colArr = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowArr.append(i)
                    colArr.append(j)
                    
        for i in rowArr:
            for j in range(cols):
                matrix[i][j] = 0
        print(matrix)

        for i in range(rows):
            for j in colArr:
                matrix[i][j] = 0
        print(matrix)
        # print(rowArr)
        # print(colArr)

solution = Solution()
solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])