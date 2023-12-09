class Solution:
    ''' 26 ms, 97.95% 13.8 MB, 67.99% '''
    ''' 
        time: O(log(x))
        space: O(1)
    '''

    def reverse(self, x: int) -> int:
        result = ''
        for i in str(x):
            if i == '-':
                continue
            else:
                result = i+result
        result = int(result)
        if x < 0:
            result = -result
        if result < -2147483648 or result > 2147483647:
            return 0
        return result


class Solution:
    ''' 32 ms, 91.74% 13.9 MB, 67.25% '''
    ''' 
        time: O(log(n))
        space: O(1)
    '''

    def reverse(self, x: int) -> int:
        negative = True if x < 0 else False
        x = -x if x < 0 else x
        remain = 0
        result = 0
        while x > 0:
            remain = x % 10
            result += remain
            x = x-remain
            if x == 0:
                break
            x = int(x/10)
            result *= 10
        result = result if -(2**31)-1 < result < 2**31 else 0
        return -result if negative else result
