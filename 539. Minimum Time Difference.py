class Solution:
    ''' 85 ms, 69.99% 17.3 MB, 36.69% '''
    ''' 
    time: O(n+nlogn+n), original: O((n-1)(n-2)...)
    space: O(n)
    '''

    def findMinDifference(self, timePoints: List[str]) -> int:
        table = []
        for i in range(len(timePoints)):
            cur = int(timePoints[i][0:2])*60+int(timePoints[i][3:])
            table.append(cur)

        table.sort()
        diff = 1440
        for i in range(len(table)-1):
            b = table[i+1]-table[i]
            diff = b if b < diff else diff

        b = table[-1]-1440-table[0]
        b = -b if b < 0 else b
        diff = b if b < diff else diff

        return diff


class Solution:
    ''' timeout '''
    ''' 
    time: O((n-1)+(n-2)+...) >> O(N^2)
    space: O(n)
    '''

    def findMinDifference(self, timePoints: List[str]) -> int:
        table = []
        for i in range(len(timePoints)):
            cur = int(timePoints[i][0:2])*60+int(timePoints[i][3:])
            table.append(cur)
        # print(table)
        diff = 1440
        n = len(table)-1
        mini = 0
        for i in range(n):
            j = i+1
            while j <= n:
                b = table[i]-table[j]
                b = b if b >= 0 else -b
                b = 1440-b if b >= 720 else b
                diff = b if b < diff else diff
                # print(diff)
                j += 1

        return diff
