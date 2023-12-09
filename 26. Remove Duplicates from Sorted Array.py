class Solution:
    ''' 96 ms, 80.83% 15.5 MB, 64.63% '''
    ''' 
    time: O(n)
    space: O(1), the flag
    '''

    def removeDuplicates(self, nums: List[int]) -> int:
        flag = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[flag] = nums[i+1]
                flag += 1
        return flag
