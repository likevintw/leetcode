

# 104 ms, 5.14%, 15.4 MB, 52.29% 
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        ans = ""
        wrap = ""
        for i in letters:
            if ord(i)>ord(target):
                if ans == "": ans = i
                if ord(i)<ord(ans): 
                    ans = i
                    break
            elif ord(i)<ord(target):
                if wrap == "": wrap = i
                if ord(i)<ord(wrap): 
                    wrap = i
                    break
        if ans == "": return wrap
        return ans

if __name__ == "__main__":
    tester = SolutionA()