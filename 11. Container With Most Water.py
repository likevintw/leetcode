
class Solution:
    ''' 700 ms, 97.01% 27.5 MB, 59.17% '''
    ''' it's better if do not use max and min '''

    def maxArea(self, height: List[int]) -> int:
        val, result, left, right = 0, 0, 0, len(height)-1
        while (left < right):
            val = height[left] if height[left] < height[right] else height[right]
            result = val*(right-left) if val*(right-left) > result else result
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result


class Solution:
    ''' 799 ms, 78.83% 27.6 MB, 18.40% '''

    def maxArea(self, height: List[int]) -> int:
        a, b = 0, len(height)-1
        result = 0
        while a < b:
            result = max(result, min(height[a], height[b])*(b-a))
            if height[a] > height[b]:
                b -= 1
            else:
                a += 1
        return result
