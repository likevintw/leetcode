class Solution:
    ''' 24 ms, 98.65% 13.9 MB, 25.87% '''
    ''' table 
        time:   O(n)
        space:  O(n)
    '''

    def wordPattern(self, pattern: str, s: str) -> bool:
        table = {}
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        i = 0
        for c in s:
            if i > len(pattern)-1:
                return False
            if pattern[i] in table.keys():
                if table[pattern[i]] != c:
                    return False
            else:
                if c in table.values():
                    return False
                table[pattern[i]] = c
            i += 1
        return True
