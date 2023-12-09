
# Newton Method
# 16 ms, 72.41%, 13.4 MB, 16.18% 
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        quotient = n
        remainder = 0
        
        while True:
            remainder = quotient % 26
            quotient = quotient / 26
            if remainder == 0: 
                quotient = quotient -1
                ans =  "Z" + ans
            else: ans =  chr(remainder+64) + ans
            if quotient == 0:break
        
        return ans

if __name__ == "__main__":
    tester = SolutionA()