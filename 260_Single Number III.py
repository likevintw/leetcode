

# 1824 ms, 7.20%, 14.8 MB, 61.67% 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _buffer = 0
        ans = []
        for i in range(len(nums)):
            if len(nums)==0: break
            _buffer = nums.pop(0)
            print(_buffer)
            if _buffer in nums: 
                while(_buffer in nums): nums.remove(_buffer)
            else: ans.append(_buffer)
        return ans

if __name__ == "__main__":
    tester = SolutionA()