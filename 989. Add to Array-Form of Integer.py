

# 280 ms, faster than 85.39%, 15.2 MB, less than 58.33%
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        # reference
        return list(str(K + int("".join(map(str, A)))))


# 3448 ms, faster than 7.99%, 15.4 MB, less than 13.01%
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        buffer = 1
        res = 0
        for i in range(len(A)):
            res += A[len(A)-i-1] * buffer
            buffer *= 10
        buffer = res + K
        res = []
        
        while True:
            if buffer == 0 and len(res)>0 : break
            res = [buffer%10] + res
            buffer = int(buffer//10)
        return res