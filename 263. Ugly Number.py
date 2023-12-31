


# 32 ms, faster than 70.05, 14.2 MB, less than 49.84%
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0: return False
        if num == 1: return True
        if num%2 == 0: return self.isUgly(num//2)
        elif num%3 == 0: return self.isUgly(num//3)
        elif num%5 == 0: return self.isUgly(num//5)
        else: return False