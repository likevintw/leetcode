
# kevin
# 60 ms, 92.00%, 15.9 MB, 5.98%
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        i, j = 0, 0
        for i in range(len(nums)):
            if nums[i] == target: 
                ans.append(i)
                for j in range(i,len(nums)):
                    if nums[j] != target:
                        ans.append(j-1)
                        break
                break
        if len(ans) == 0: return [-1,-1]
        elif len(ans) < 2:return [i,j]
        else: return ans


if __name__ == "__main__":
    pass