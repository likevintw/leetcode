class Solution:
    '''
    65 ms, faster than 19.94%,14 MB, 82.56%
    space: O(n), word lengh
    time: O(N)
    '''

    def reverseWords(self, s: str) -> str:
        result, buffer = "", ""
        tail_flag = False
        for i in range(len(s)):
            if s[i] == " ":
                if buffer == "":
                    continue
                if i == len(s)-1:
                    result = buffer+result
                else:
                    result = " "+buffer+result
                buffer = ""
                tail_flag = True
            else:
                buffer = buffer+s[i]
                tail_flag = False
        if not buffer == "":
            result = buffer+result
        if tail_flag:
            result = result[1:]
        return result
