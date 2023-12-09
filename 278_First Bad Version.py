
# 16 ms, 70.67%, 13.5 MB, 37.84% 
# 24 ms, 36.40%, 13.3 MB, 65.04% 
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def movement (k):
            k = int(k/2)
            if k > 1: return k
            else: return 1
        i = 0
        move = n
        while(True):
            if isBadVersion(i+1) != isBadVersion(i): return i+1
            elif isBadVersion(i+1) == True:  i = i - movement(move)
            elif isBadVersion(i+1) == False: i = i + movement(move) 
            # print(i+1,isBadVersion(i+1) , move)
            move = movement(move)
            # print(i+1, isBadVersion(i+1))
            
        # for i in range(n): print(i+1, isBadVersion(i+1))


if __name__ == "__main__":
    tester = SolutionA()