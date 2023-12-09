# 36 ms, 74.74%,14 MB, 12.83%
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table = {}
        result = 0
        for i in jewels:
            if i not in table.keys():
                table.update({i: 1})
        for i in stones:
            if i in table.keys():
                result += 1
        return result
