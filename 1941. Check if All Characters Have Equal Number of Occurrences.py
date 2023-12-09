

# 63 ms, 22.54% , 13.8 MB, 79.84%
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        table = {}
        for i in s:
            if i in table.keys():
                table.update({i: table[i]+1})
            else:
                table.update({i: 1})
        buffer = None
        for i in table.keys():
            if not buffer:
                buffer = table[i]
            else:
                if not buffer == table[i]:
                    return False
        return True


# reference
# 36 ms,   85.62%  13.8 MB, less than 79.84%


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
