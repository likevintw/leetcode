

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        size_s = len(s)
        size_p = len(p)
        checked = 0
        for i in range(size_p):
            for j in range(size_s):
                if p[i]==s[j] or p[i]== '*': 
                    checked = checked + 1
                    print(s[j])
                    print(p[i])
                    if checked == size_p:
                        if j == size_s-1: return True
                        else: return False
        return False


if __name__ == "__main__":
    tester = Solution()
    #print(tester.isMatch('abcsss','c*'))
    print(tester.isMatch('aa','a'))
    print(tester.isMatch('aa','a*'))