

class Solution:
    ''' 37 ms, 75.09% 13.8 MB, 97.59% '''
    '''
    time:   O(n)
    space:  O(1)
    '''

    def removeElement(self, nums: List[int], val: int) -> int:
        s, f = 0, 0
        while f < len(nums):
            if nums[f] != val:
                nums[s] = nums[f]
                s += 1
            f += 1
        return s


class Solution:
    ''' 38 ms, 73.43% 13.9 MB, 15.96% '''
    '''
    time:   less than O(n)
    space:  O(1)
    '''

    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return i
