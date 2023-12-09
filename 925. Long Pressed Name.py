
# reference
# 24 ms, 41.81%, 13.6 MB, 40.09%
class SolutionA(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        cnt = 0 
        answer = False 
        for i in range(len(typed)): 
            if cnt < len(name) and name[cnt] == typed[i]: 
                cnt = cnt + 1 
            elif i == 0 or typed[i] != typed[i-1]: 
                return answer
        if cnt == len(name): 
            answer = True 
        return answer

# kevin
# 48 ms, 6.47%, 13.5 MB, 40.09%
class SolutionB(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        j = 0
        latest_char = ""
        if len(name) > len(typed): return False
        for i in range(len(typed)):
            print(i, j, typed[i], name[j], len(name))
            if j < len(name) and typed[i] == name[j]:
                if j < len(name)-1: j = j + 1
            elif i == 0 or typed[i] != typed[i-1]:
                    return False
        if j != len(name):
            if name[len(name)-1] != typed[len(typed)-1]: return False
        return True

# BB Yao
# 44 ms, 6.47%, 13.5 MB, 40.09%
class SolutionC(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        res = False
        latest = ""
        start = 0
        for i in range(len(typed)):
            for j in range(start, len(name)):
                print(i,j,typed[i],name[j])
                if typed[i] != name[j]:
                    if typed[i] != latest: return False
                    else: break
                else:
                    latest = name[j]
                    if j + 1 < len(name) : start = j + 1
                    else: res = True
                    break
        return res

if __name__ == "__main__":
    tester = SolutionA()