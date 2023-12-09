

# 196 ms, 59.41%, 16.4 MB,37.41%
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        
        c = [0] * 60   # array for the remainder
        res = 0
        
        for j in time:
            res += c[ -j % 60 ]
            c[j % 60] += 1
        return res


if __name__ == "__main__":
    tester = SolutionA()