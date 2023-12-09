
# reference
# 52 ms,80.32%,13.9 MB, 23.39%
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        for i in reversed(range(len(arr))):
            if arr[i] == 0: arr.insert(i,0); arr.pop()


if __name__ == "__main__":
    tester = SolutionA()