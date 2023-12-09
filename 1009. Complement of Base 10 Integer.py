

# 24 ms, faster than 96.38%, 14.1 MB, less than 92.59%
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        res = ""
        for i in bin(N)[2:]: res+="0" if i=="1" else "1"
        return int(res,2)
