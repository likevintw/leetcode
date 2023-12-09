
import sys


#
class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c == ')':
                signs.pop()
            i += 1
        return total


tester = Solution()
print(tester.calculate("-2+1"))
print(tester.calculate("2147483647"))
print(tester.calculate("1 + 1"))
print(tester.calculate(" 2-1 + 2 "))
print(tester.calculate("(1+(4+5+2)-3)+(6+8)"))
print(tester.calculate("- (3 + (4 + 5))"))
print(tester.calculate("4+5+2"))
print(tester.calculate("(1+(4+5+2)-3)+(6+8)"))
print(tester.calculate("1-(+1+1)"))
