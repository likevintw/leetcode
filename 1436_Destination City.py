

# 180ms, 5.16%, 13.4 MB, 53.55%
class SolutionA(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        check = []
        ans = []
        flag = 0
        for i in paths:
            for j in range(len(i)):
                print(j,i[j],check,ans)
                if i[j] in check:
                    check.remove(i[j])
                    if i[j] in ans: ans.remove(i[j])
                else: 
                    check.append(i[j])
                    if j == 1: ans.append(i[j])
        return ans[0]

# 28 ms, 99.57 %, 13.6 MB, 53.55%
class SolutionB(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        src = [i[0] for i in paths]
        dist = [i[1] for i in paths]
        for i in dist:
            if i not in src: return i


if __name__ == "__main__":
    tester = SolutionA()