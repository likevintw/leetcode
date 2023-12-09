class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        # add checking
        for i in range(1, len(s)):
            for j in range(i-1, -1, -1):
                # print(i,j)
                if (i+j) > len(s)-1 or j < 0:
                    break
                if s[j] == s[i+j]:
                    if (i+1) > len(result):
                        result = s[j:i+j+1]
                        # print(result)
                        continue
                else:

                    break
        # print(result)

        return result
