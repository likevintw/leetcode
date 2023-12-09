


# reference
# 452 ms, faster than 83.67% ,14.5 MB, less than 44.42%
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(1,len(arr) + 1):
            end = i - 1 
            start = max(i-1-k,-1)
            currMax = 0
       
            for p in range(end, start, -1):
                currMax = max(currMax,arr[p])
                dp[i] = max(dp[i], dp[p] + currMax * (i-p))

        return dp[-1]


# kevin3
# 448 ms, faster than 84.46%, 14.3 MB, less than 88.05%
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        dp = [0]*(len(arr))
        
        dp[0] = arr[0]
        
        max_arr = 0
        max_res = 0
            
        for i in range(1,len(arr)):
            max_res, max_arr = 0,0
            position = k if i >= k  else  i+1
            for j in range(position): 
                max_arr = max(arr[i-j], max_arr)
                max_res = max(dp[i-(j+1)]+max_arr*(j+1),max_res)
            dp[i] = max_res
            
        return dp[len(dp)-1]

# kevin2
#  424 ms, faster than 86.45%, 14.5 MB, less than 44.42% 
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        dp = [0]*(len(arr))
        
        dp[0] = arr[0]
        
        buffer = []
        max_arr = 0
        position = 0
            
        for i in range(1,len(arr)):
            buffer, max_arr = [],0
            position = k if i >= k  else  i+1
            for j in range(position): 
                max_arr = max(arr[i-j], max_arr)
                buffer.append(dp[i-(j+1)]+max_arr*(j+1))
            dp[i] = max(buffer)
            
        return dp[len(dp)-1]

# kevin1
# 1708 ms, faster than 20.32% ,14.3 MB, less than 88.05% 
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        dp = [0]*(len(arr))
        
        dp[0] = arr[0]
        
        buffer, max_arr = [],[]
        position = 0
            
        for i in range(1,len(arr)):
            buffer, max_arr = [],[]
            position = k if i >= k  else  i+1
            for j in range(position): 
                max_arr.append(arr[i-j])
                buffer.append(dp[i-(j+1)]+max(max_arr)*(j+1))
            dp[i] = max(buffer)
            
        return dp[len(dp)-1]

