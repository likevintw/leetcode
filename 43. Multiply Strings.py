class Solution:
    ''' 69 ms, 58.41% 14 MB, 31.95% '''
    '''
    time:   O(i+j+k)
    space:  O(1)
    '''

    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        result = ''
        i = 0
        while True:
            n1 += int(num1[i])
            if i == len(num1)-1:
                break
            n1 *= 10
            i += 1
        i = 0
        while True:
            n2 += int(num2[i])
            if i == len(num2)-1:
                break
            n2 *= 10
            i += 1
        n = n1*n2
        if n == 0:
            return '0'
        while n > 0:
            result = str(n % 10)+result
            n -= n % 10
            n //= 10
        return result
