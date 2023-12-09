class Solution:
    '''
    53 ms, 65.49% 14 MB, 92.39%
    '''

    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        b = 0
        for i in nums:
            b += i
            result.append(b)
        return result
