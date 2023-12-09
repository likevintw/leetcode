

class Solution:
    ''' 48 ms, 93.19% 14 MB, 38.52%'''

    def intToRoman(self, num: int) -> str:
        number = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        table = {}
        table[1] = 'I'
        table[4] = 'IV'
        table[5] = 'V'
        table[9] = 'IX'
        table[10] = 'X'
        table[40] = 'XL'
        table[50] = 'L'
        table[90] = 'XC'
        table[100] = 'C'
        table[400] = 'CD'
        table[500] = 'D'
        table[900] = 'CM'
        table[1000] = 'M'
        result = ''
        while num > 0:
            for i in number:
                if num >= i:
                    num = num-i
                    result = result+table[i]
                    break
        return result
