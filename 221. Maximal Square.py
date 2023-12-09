class Solution:
    '''
    706 ms, 52.40% 16.6 MB, 37.90%
    '''

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        maxi = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i > 0 and j > 0:
                        matrix[i][j] = min(
                            int(matrix[i-1][j-1]), int(matrix[i-1][j]), int(matrix[i][j-1]))+1
                        if matrix[i][j] > maxi:
                            maxi = matrix[i][j]
                    elif maxi == 0:
                        maxi = 1
        return maxi*maxi
