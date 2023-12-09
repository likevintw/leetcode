
# kevin
# 136 ms, faster than 80.99%, 14.2 MB, less than 92.96%
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2,i3,i5 = 0,0,0
        r2,r3,r5 = 2,3,5
        ugly = [1]
        for i in range(n):
            ugly.append(min(r2,r3,r5))
            if ugly[-1] == r2: 
                i2+=1; r2=ugly[i2]*2
            if ugly[-1] == r3: 
                i3+=1; r3=ugly[i3]*3
            if ugly[-1] == r5: 
                i5+=1; r5=ugly[i5]*5
        return ugly[n-1]

# kevin
# 120 ms, faster than 88.52%, 14.2 MB, less than 92.96% 
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2,i3,i5 = 0,0,0
        r2,r3,r5 = 2,3,5
        ugly = [1]
        buffer = 0
        for i in range(n):
            buffer = min(r2,r3,r5)
            # print(buffer,r2,r3,r5)
            ugly.append(buffer)
            if buffer == r2: 
                i2+=1; r2=ugly[i2]*2
            if buffer == r3: 
                i3+=1; r3=ugly[i3]*3
            if buffer == r5: 
                i5+=1; r5=ugly[i5]*5
        return ugly[n-1]

# reference
# 128 ms, faster than 86.48% , 14.4 MB, less than 26.97% 
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n # To store ugly numbers  
        ugly[0] = 1
        i2 = i3 = i5 = 0

        # set initial multiple value 
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        for l in range(1, n): 
            ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5) 
            if ugly[l] == next_multiple_of_2: 
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2
            if ugly[l] == next_multiple_of_3: 
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3
            if ugly[l] == next_multiple_of_5:  
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5
        return ugly[-1]