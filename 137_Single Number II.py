


# 44  ms, 68.21%, 14.9 MB, 72.23% 
# GOD
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        two = 0
        for i in nums:
            one = (one^i)&(~two);
            two = (two^i)&(~one);
        return one

# kevin
# 1356  ms, 5.03%, 15.1 MB, 46.68% 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _buffer = 0
        for i in range(len(nums)):
            _buffer = nums.pop(0)
            if _buffer in nums: 
                while(_buffer in nums): nums.remove(_buffer)
            else: return _buffer

if __name__ == "__main__":
    tester = SolutionA()