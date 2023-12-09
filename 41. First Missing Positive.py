class Solution:
    ''' 986 ms, 75.95% 59.6 MB, 85.51% '''
    '''
    time:   O(n*n), but discuss said O(n)
    space:   O(1)
    '''

    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                buffer = nums[i]
                nums[i], nums[buffer-1] = nums[buffer-1], buffer
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
