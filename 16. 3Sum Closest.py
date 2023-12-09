
# 342 ms, 47.10%, 14 MB, 70.68%
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        j, k = 0, 0
        best = 0
        diff = 0
        best_diff = None

        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                if not j < k:
                    break
                s = nums[i]+nums[j]+nums[k]
                diff = abs(s-target)
                if not best_diff:
                    best_diff = diff
                    best = s
                if diff < best_diff:
                    best_diff = diff
                    best = s
                if s == target:
                    return target
                elif s > target:
                    k -= 1
                else:
                    j += 1
        return best
