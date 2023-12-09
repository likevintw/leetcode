
# XOR
# 100 ms, 67.35%, 15.6 MB, 9.70% 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums: res ^= i
        return res

# 1556  ms, 12.48%, 15 MB, 84.71% 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _buffer = 0
        for i in range(len(nums)):
            _buffer = nums.pop(0)
            if _buffer in nums: nums.remove(_buffer)
            else: return _buffer

if __name__ == "__main__":
    tester = SolutionA()