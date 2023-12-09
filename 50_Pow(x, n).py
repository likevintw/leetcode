
# kevin
# 12 ms, 95.66%, 13.3 MB, 92.91%
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        _flag = True
        if n < 0:
            n = -n
            _flag = False
        rem = []
        while True:
            rem.insert(0, n%2)
            n = int(n / 2)
            if n <= 1: rem.insert(0, n%2); break
        
        a, b = 1, 1
        k = len(rem)-1
        for i in range(len(rem)):
            if i == 0: a *= x
            else: a *= a
            if rem[k-i] ==1: b = b * rem[k-i] * a
        
        if _flag == False: return 1/b
        else: return b

# others
# 28 ms, 20.31%, 13.6 MB, 7.54%
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        div = False
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n < 0:
            n = -n
            div = True
        ops = []
        while n > 1:
            if n % 2:
                ops.append(False)
                n -= 1
            else:
                ops.append(True)
                n //= 2
        ops = ops[::-1]
        res = x
        for op in ops:
            if op:
                res *= res
            else:
                res *= x
        return 1 / res if div else res

if __name__ == "__main__":
    pass