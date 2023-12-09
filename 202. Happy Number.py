

class Solution:
    ''' 41 ms, 69.74% 13.8 MB, 63.87%  '''
    ''' fast and slow pointer '''

    def isHappy(self, n: int) -> bool:
        def get_square_sum(n):
            s = 0
            while n > 0:
                r = n % 10
                s += r*r
                n -= r
                n = int(n/10)
            return s

        s = n
        f = n
        while True:
            s = get_square_sum(s)
            f = get_square_sum(get_square_sum(f))
            if s == f:
                break
        return s == 1


class Solution:
    ''' 42 ms, 67.52% 13.8 MB, 63.87% '''
    ''' log(n), table '''

    def isHappy(self, n: int) -> bool:
        def get_square_sum(n):
            s = 0
            while n > 0:
                r = n % 10
                s += r*r
                n -= r
                n = int(n/10)
            return s

        i = n
        table = []
        while True:
            i = get_square_sum(i)
            if i in table:
                return False
            table.append(i)
            if i == 1:
                return True


class Solution:
    def isHappy(self, n: int) -> bool:
        ''' not a valided solution '''
        ''' 34 ms, 89.74% 13.7 MB, 97.17% '''
        if n == 1 or n == 7:
            return True
        if len(str(n)) == 1:
            return False
        else:
            return self.isHappy(sum(int(word)**2 for word in str(n)))
