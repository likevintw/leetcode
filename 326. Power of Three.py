


# 68 ms, faster than 89.02%, 14.2 MB, less than 78.94%
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0: return False
        if n==1: return True
        if n%3==0: return self.isPowerOfThree(n/3)
        else: return False
        