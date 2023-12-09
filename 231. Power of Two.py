
# 32 ms, faster than 69.37%, 14.2 MB, less than 42.77%
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0: return False
        if n==1: return True
        if n%2==0: return self.isPowerOfTwo(n//2)
        else: return False