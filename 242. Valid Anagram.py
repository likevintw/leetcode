
# 44 ms, faster than 80.61%, 15 MB, less than 12.28%
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t): return True
        else: return False