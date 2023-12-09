class Solution:
    ''' 26 ms, 97.77% 13.9 MB, 82.01% '''
    '''
    time:   O(m*n)
    space:  O(1)
    '''

    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                for j in range(0, len(needle)):
                    if haystack[i+j] != needle[j]:
                        break
                    if j == len(needle)-1:
                        return i
        return -1
