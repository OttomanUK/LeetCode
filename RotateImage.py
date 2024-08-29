class Solution(object):
    def rotate(self, matrix):
        rows = len(matrix)
        for i in range(rows):
            for j in range(i,rows):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 

        for i in range(rows):
            left = 0
            right = rows - 1
            while left < right:
                matrix[i][left],matrix[i][right] = matrix[i][right], matrix[i][left]
                left = left + 1
                right = right - 1
        print(matrix)
            

solution = Solution()
solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])