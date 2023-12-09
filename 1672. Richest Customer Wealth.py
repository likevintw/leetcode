

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        buffer = 0
        for i in accounts:
            buffer = sum(i)
            maxi = buffer if buffer>maxi else maxi
        return maxi