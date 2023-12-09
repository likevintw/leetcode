class Solution:
    ''' reference '''
    ''' 39 ms, 92.55% 14 MB, 85.01% '''

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def swap(nums, i, begin):
            temp = nums[i]
            nums[i], nums[begin] = nums[begin], nums[i]

        def upset(nums, begin, result):
            if begin == len(nums):
                temp = []
                for i in range(len(nums)):
                    temp.append(nums[i])
                result.append(temp)
                return
            for i in range(begin, len(nums)):
                swap(nums, i, begin)
                upset(nums, begin + 1, result)
                swap(nums, i, begin)
        upset(nums, 0, result)
        return result


class Solution:
    ''' reference '''
    ''' 51 ms, 58.98% 14.1 MB, 59.38% '''

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def upset(nums, begin, result):
            if begin == len(nums):
                temp = []
                for i in range(len(nums)):
                    temp.append(nums[i])
                result.append(temp)
                return
            for i in range(begin, len(nums)):
                nums[i], nums[begin] = nums[begin], nums[i]
                upset(nums, begin + 1, result)
                nums[i], nums[begin] = nums[begin], nums[i]
        upset(nums, 0, result)
        return result
