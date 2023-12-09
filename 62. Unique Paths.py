class Solution:
    ''' 28 ms, 96.07% 13.9 MB, 77.83%'''
    ''' formula solution '''
    ''' 
        time: O(m)
        space O(1)
    '''

    def uniquePaths(self, m: int, n: int) -> int:
        N = n + m - 2
        k = m - 1
        res = 1
        for i in range(1, k+1):
            res = res * (N - k + i) / i
        return int(res)


class Solution:
    ''' dp '''
    ''' 36 ms, 77.61% 13.9 MB, 77.83% '''
    ''' 
        time: O(m*n)
        space O(n)
    '''

    def uniquePaths(self, m: int, n: int) -> int:
        result = [1]*n
        for i in range(m):
            if i == 0:
                continue
            for j in range(n):
                if j == 0:
                    continue
                result[j] = result[j]+result[j-1]
        return result[n-1]


class Solution:
    ''' dp '''
    ''' 34 ms, 80.81% 13.8 MB, 77.83% '''
    ''' 
        time:   O(m * n)
        space:  O(m * n), 如果只有做最後一列，那可以做到O(m)
    '''

    def uniquePaths(self, m: int, n: int) -> int:
        result = [[0]*n]*m
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    result[i][j] = 1
                    continue
                result[i][j] = result[i-1][j]+result[i][j-1]
        return result[m-1][n-1]
