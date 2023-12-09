

class Solution:
    ''' table '''
    ''' 57 ms, 95.49% 15.1 MB, 51.64% '''
    ''' 
        time: O(n)
        space: O(n)
    '''

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in table.keys():
                return i, table[diff]
            table[nums[i]] = i


class Solution:
    ''' Exhaustive Method '''
    ''' without build table '''
    '''
        time: O(n^2)
        space: O(1)
    '''

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in nums:
                for j in range(i+1, len(nums), 1):
                    if nums[j] == target-nums[i]:
                        return [i, j]
