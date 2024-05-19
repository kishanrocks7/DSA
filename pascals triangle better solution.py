class Solution:
    def ncr(self, n, r):
        res = 1
        if r == 0 or r == n:
            return 1
        else:
            for i in range(1, r + 1): 
                res = res * (n + 1 - i) // i  
        return res

    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                row.append(self.ncr(i, j))
            triangle.append(row)
        return triangle
