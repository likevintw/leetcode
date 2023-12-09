class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        buffer = 0
        for i in range(len(A)):
            buffer = A.pop(0)
            if buffer in A: return buffer