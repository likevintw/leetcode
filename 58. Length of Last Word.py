class Solution:
    ''' 29 ms, 87.83%  14 MB,  40.08% '''
    '''
    time:   O(n)
    space:  O(1)
    '''

    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = len(s)-1
        result = 0
        while n >= 0:
            if s[n] == ' ':
                if result != 0:
                    return result
            else:
                result += 1
            n -= 1
        return result


class Solution:
    ''' 32 ms, 53.83% ,14.4 MB, 7.49% '''

    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if s[i] == " ":
                if i == len(s)-1:
                    break
                if s[i+1] and s[i+1] == " ":
                    continue
                res = 0
            else:
                res += 1
        return res
