

# 28 ms, faster than 87.34%, 14.2 MB, less than 71.90%
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0: return False
        if n==1: return True
        if n%4==0: return self.isPowerOfFour(n/4)
        else: return False
        