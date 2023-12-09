

# 45 ms, ,46.78% , 13.8 MB, less than 72.20%
class Solution:
    def countPoints(self, rings: str) -> int:
        table = {}
        result = 0
        for n in range(0, len(rings), 2):
            if rings[n+1] in table.keys():
                e = table[rings[n+1]]
                if rings[n] not in e:
                    e.append(rings[n])
                    table.update({rings[n+1]: e})
                    if len(e) == 3:
                        result += 1
            else:
                table.update({rings[n+1]: [rings[n]]})
        return result


# reference
# 39 ms,  63.64% , 13.8 MB,  72.20%
class Solution:
    def countPoints(self, rings: str) -> int:
        h = defaultdict(set)
        for i in range(0, len(rings) - 1, 2):
            h[rings[i + 1]].add(rings[i])
        return sum(len(v) == 3 for v in h.values())
