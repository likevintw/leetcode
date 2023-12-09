
# kevin
# 92 ms, 5.15%, 13.5 MB, 94.15%
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans = []
        jump = len(nums)-1
        i = 0
        for j in range(len(nums)):
            print(i)
            ans.append(nums[i])
            i += n
            if i >= len(nums): i -= jump
        return ans

if __name__ == "__main__":
    tester = SolutionA()