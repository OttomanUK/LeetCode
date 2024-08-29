class Solution(object):
    def spiralOrder(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        direction = 1
        result = []
        row = 0
        col = -1

        while rows > 0 and cols > 0:
            for i in range(cols):
                col = col + direction
                result.append(matrix[row][col])
            rows = rows - 1

            for j in range(rows):
                row = row + direction
                result.append(matrix[row][col])
            cols = cols - 1

            direction = direction * -1 

        print(result)

solution = Solution()
solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


