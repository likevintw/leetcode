

class Solution:
    '''  40 ms, 98.36% 13.8 MB, 80.54% '''

    def romanToInt(self, s: str) -> int:
        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        result = table[s[0]]
        for i in range(len(s)-1):
            if table[s[i]] < table[s[i+1]]:
                result -= 2*table[s[i]]
            result += table[s[i+1]]
        return result
