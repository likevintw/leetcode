


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def smaller(_x,_y):return _x if _x < _y else _y
        
        dp = []
        for i in range(len(cost)): dp.append(0)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)):
            dp[i]=smaller(dp[i-1],dp[i-2])+cost[i]
        return smaller(dp[len(cost)-1],dp[len(cost)-2])