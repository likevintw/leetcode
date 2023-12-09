
class Solution:
    ''' 54 ms, 35.91% 14.1 MB, 80.60% '''

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in nums:
            for j in result:
                result = result+[j+[i]]
        return result


class Solution:
    ''' 24 ms, 99.82% 13.9 MB, 95.77% '''

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in nums:
            result += [j+[i] for j in result]
        return result


class Solution:
    ''' offical solution '''
    ''' 40 ms,  73.38% 13.9 MB 95.77%'''

    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output
