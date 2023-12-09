

class Solution:
    ''' 48 ms, 52.23% ,13.9 MB, 77.48% '''

    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2)+int(b, 2))[2:]


class Solution:
    ''' 49 ms, 48.91% 13.9 MB, 27.89%'''

    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        sa, sb = '', ''
        result = ''
        while True:
            if len(a) > 0:
                sa = a[-1]
                a = a[:-1]
            else:
                sa = 0
            if len(b) > 0:
                sb = b[-1]
                b = b[:-1]
            else:
                sb = 0
            buffer = carry+int(sa)+int(sb)
            result = str(buffer % 2)+result
            if buffer >= 2:
                carry = 1
            else:
                carry = 0
            if len(a) == 0 and len(b) == 0:
                break
        if carry == 1:
            result = str(carry)+result
        return result


class Solution:
    '''
    # 36 ms, 85.14%, 13.9 MB,  28.91%
    '''

    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        ma = 0
        mb = 0
        result = ""
        carry = 0
        check = 0
        while True:
            ma, mb = 0, 0
            if i >= 0 and a[i] == '1':
                ma = 1
            if j >= 0 and b[j] == '1':
                mb = 1
            check = ma+mb+carry
            result = str(check % 2)+result
            carry = int(check/2)
            # print(g,ma,mb,check,carry,result)
            if i <= 0 and j <= 0 and carry == 0:
                break
            i -= 1
            j -= 1
        return result


class Solution:
    '''
    60 ms,  25.00% ,13.8 MB, 77.48%
    '''

    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        ma, mb = 0, 0
        result = ""
        carry, check = 0, 0
        while True:
            ma, mb = 0, 0
            if i >= 0 and a[i] == '1':
                ma = 1
            if j >= 0 and b[j] == '1':
                mb = 1
            check = ma+mb+carry
            result = str(check % 2)+result
            carry = int(check/2)
            # print(g,ma,mb,check,carry,result)
            if i <= 0 and j <= 0 and carry == 0:
                break
            i -= 1
            j -= 1
        return result
