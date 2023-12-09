# 52 ms, 39.54%, 14.5 MB, 92.89%
class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        head, tail = 0, len(s)-1
        while head < tail:
            while head < tail and not s[head].isalnum():
                head += 1
            while head < tail and not s[tail].isalnum():
                tail -= 1
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
        return True