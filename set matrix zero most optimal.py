class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        columns = len(matrix[0])
        first_column_zero = False

        for i in range(rows):
            if matrix[i][0] == 0:
                first_column_zero = True
            for j in range(1, columns):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(rows - 1, -1, -1):
            for j in range(columns - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if first_column_zero:
                matrix[i][0] = 0


        """LOGIC: To store if a column or row to be zeroed out or not we are using first row and first column of
        matrix itself insted of a external list ( to reduce space complexity ).
        but for matrix[0][0] we will store in a variable as being an intersection it will cause error so it will
        be changed at very end.
        also we are have to check if first column to be zeroed or not separetly bcause only first row is getting checked
        in the initial logic."""