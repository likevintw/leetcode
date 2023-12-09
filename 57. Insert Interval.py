
# 64 ms, 99.78%, 17.5 MB, 31.05% (17.4 MB, 91.68%)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if len(intervals) == 0: return [newInterval]
        
        left, right = newInterval[0], newInterval[1]
        flag = 0
        for e in intervals:
            if newInterval[0] > e[1] or newInterval[1] < e[0]:
                res.append(e)
            else: 
                if e[0] < left: left = e[0]
                if e[1] > right: right = e[1]
        # print(left,right)
        # print(res)
        for i in range(len(res)):
            if flag == 0 and right < res[i][0]:
                flag = 1
                res.insert(i,[left,right])
                break
        if flag == 0: res.append([left,right])
        return res
