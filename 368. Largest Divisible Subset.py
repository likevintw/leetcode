class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # nums = [5,9,18,54,108,540,90,180,360,720]
        
        nums.sort()
        ans = []
        dp = []
        for i in nums:dp.append([i])
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(dp[j])>=len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
            if len(dp[i])>len(ans): ans = dp[i] 
        # print(dp)
        return(ans)