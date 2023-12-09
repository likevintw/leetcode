

# 24 ms, faster than 97.49%, 14.2 MB, less than 46.66%
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = list(str(int("".join(map(str, digits)))+1))
        if digits[0] == 0:
            res = (len(digits)-len(res))*[0]+res
        return res

# explaintion:
# 24 ms, 96.69%, 14.2 MB, 46.09%


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # integer to string list
        buffer = list(map(str, digits))

        # string list to a string
        buffer1 = "".join(buffer)
        # print(buffer1)

        # string to integer and plus one
        buffer2 = int(buffer1)+1
        # print(buffer2)

        # integer to a string then to string list
        res = list(str(buffer2))
        # print(res)

        if len(digits) == 0:
            res = (len(digits)-len(res))*[0]+res
        return res
