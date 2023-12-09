

# 12 ms, 91.04%, 13.3 MB, 47.76% 
class SolutionA(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        r1,i1 = a[:-1].split("+")
        r2,i2 = b[:-1].split("+")
        r1 = int(r1)
        r2 = int(r2)
        i1 = int(i1)
        i2 = int(i2)
        #print(r1,i1,r2,i2)
        #print(r1*r2-i1*i2,r1*i2+r2*i1)
        return str(r1*r2-i1*i2)+"+"+str(r1*i2+r2*i1)+"i"


if __name__ == "__main__":
    tester = SolutionA()