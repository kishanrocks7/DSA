class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    for k in range(len(matrix[0])):
                        if matrix[i][k]!=0:
                            matrix[i][k]=-100000
                    for l in range(len(matrix)):
                        if matrix[l][j]!=0:
                            matrix[l][j]=-100000

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==-100000:
                    matrix[i][j]=0
        

""" LOGIC : Traversing through whole matrix we have marked whole row and column of that intersection as -100000.
(With the exception that node value shouldnt be originally 0).Traversing again we have turned those -100000 to 0 """
                


        