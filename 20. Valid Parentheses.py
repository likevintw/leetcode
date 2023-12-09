
# 32 ms, 58.35%, 14.4 MB, 36.10%
class Solution:
    ''' 38 ms, 69.55% 14 MB, 27.45% '''

    def isValid(self, s: str) -> bool:
        table = {")": "(", "]": "[", "}": "{"}
        stack = []
        if len(s) % 2 != 0 or len(s) == 0:
            return False
        for i in s:
            if i in ")]}":
                if len(stack) == 0:
                    return False
                if table[i] != stack.pop():
                    # print(table[i],i)
                    return False
            else:
                stack.append(i)
        if len(stack) != 0:
            return False
        return True


class Solution:
    '''
    Brute-force
    74 ms, 5.26%, 13.9 MB, 28.37% 
    '''

    def isValid(self, s: str) -> bool:
        table = {")": "(", "]": "[", "}": "{"}
        result = []
        for i in s:
            if len(result) > 0 and i in table.keys():
                if table[i] == result[-1]:
                    result.pop()
                    continue
            result.append(i)
        if len(result) == 0:
            return True
        return False


class Solution:
    ''' 39 ms, 66.99% 13.8 MB, 74.40%'''
    ''' stack 
    time:   O(N)
    space:  O(3)
    '''

    def isValid(self, s: str) -> bool:
        table = {")": "(", "]": "[", "}": "{"}
        result = []
        for i in s:
            if i in table.values():
                result.append(i)
            elif i in table.keys():
                if result == [] or table[i] != result.pop():
                    return False
            else:
                return False
        if not len(result) == 0:
            return False
        return True


class Solution:
    ''' different consequence in if loop, different result'''
    ''' 54 ms, 27.63% 13.9 MB, 27.45% '''

    def isValid(self, s: str) -> bool:
        table = {}
        table[')'] = '('
        table['}'] = '{'
        table[']'] = '['
        stack = []
        for i in s:
            if i in table.keys():
                if not table[i] in stack:
                    return False
                elif stack[-1] != table[i]:
                    return False
                else:
                    stack = stack[:-1]
            else:
                stack.append(i)
        if len(stack) != 0:
            return False
        return True
