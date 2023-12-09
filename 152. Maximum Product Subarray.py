class Solution:
    '''
    dp
    reference
    82 ms, 95.72% 15.6 MB, 9.99%
    1. 0 or 1 = 1, to eliminate the element 0
    2. there are two consequence which are from the head and the tail of nums, so need to check all of those possibility
    '''

    def maxProduct(self, nums: List[int]) -> int:
        suf = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            suf[i] *= suf[i-1] or 1
        return max(nums+suf)
