
# 注意m,n的順序
class Solution:
    '''
   108 ms, 39.50% 14.8 MB, 55.33%
    Time: O(mxn)
    Space: O(mxn)
    '''

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        result = []
        for i in range(n):
            result.append([0]*m)
        # print(result)
        for j in range(n):
            for i in range(m):
                result[j][i] = matrix[i][j]

        return result
