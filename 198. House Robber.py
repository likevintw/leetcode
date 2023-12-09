class Solution:
    '''
    dp
    reference
    34 ms, 83.72% 13.9 MB, 19.19%
    '''

    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                a = max(a+nums[i], b)
            else:
                b = max(a, b+nums[i])
        return max(a, b)


class Solution:
    '''
    dp
    reference
    38 ms, 70.14% 14 MB, 19.19% 
    '''

    def rob(self, nums: List[int]) -> int:
        last, cur = 0, 0
        for i in nums:
            cur, last = max(last+i, cur), cur
        return cur
