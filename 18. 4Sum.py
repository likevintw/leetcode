
# 1334 ms, 45.87%, 13.9 MB, 71.87%
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for r in range(len(nums)-3):
            while r > 0 and i == nums[0] and len(nums) > 1:
                i = nums.pop(0)
            if len(nums) < 4:
                break
            i = nums.pop(0)
            res = self.three_sum(nums, target-i)
            if len(res) > 0:
                for r in res:
                    result.append([i, r[0], r[1], r[2]])
        return result

    def three_sum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        j, k = 0, 0

        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                if not j < k:
                    break
                s = nums[i]+nums[j]+nums[k]
                if s == target:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif s > target:
                    k -= 1
                else:
                    j += 1
        return result
