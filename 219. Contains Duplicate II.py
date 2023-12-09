class Solution:
    '''
    779 ms, 51.28% 27.2 MB, 74.26%
    time:   O(N)
    space:  O(N)
    '''

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i in range(len(nums)):
            if nums[i] in table.keys():
                if (i-table[nums[i]]) <= k:
                    return True
            table.update({nums[i]: i})
        return False
