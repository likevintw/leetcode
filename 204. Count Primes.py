

# 92 ms, faster than 99.82%, 23.5 MB, less than 93.95%
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3: return 0
        if n==3: return 1
        n, correction = n-n%6+6, 2-(n%6>1)
        sieve = [True] * (n//3)
        for i in range(1,int(n**0.5)//3+1):
            if sieve[i]:
                k=3*i+1|1
                sieve[k*k//3 ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
                sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
        return len([2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]])
        