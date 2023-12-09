class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consis = 0
        for i in words:
            for j in range(len(i)):
                if i[j] not in allowed: break
                if j == len(i)-1: consis += 1
        return consis