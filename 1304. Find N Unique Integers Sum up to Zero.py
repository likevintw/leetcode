
# 24 ms, 98.25%, 14 MB, 100.00%
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return range(1-n, n, 2)
