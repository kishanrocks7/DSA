class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=[1]*len(matrix)
        columns=[1]*len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                 if matrix[i][j]==0:
                    rows[i]=0
                    columns[j]=0
        for i in range(len(rows)):
            if(rows[i]==0):
                for j in range(0,len(columns)):
                    matrix[i][j]=0
        for j in range(len(columns)):
            if(columns[j]==0):
                for i in range(0,len(rows)):
                    matrix[i][j]=0
        


                


"""LOGIC: In this solution we are using two lists "rows" and "columns" to store if that row/column should
0 or not and later on iterating through whole matrix to change columns/rows to zero based on stored values
in external lists(rows & columns). """