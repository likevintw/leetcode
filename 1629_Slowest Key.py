

# 32 ms,99.05%,13.7 MB,90.76%
class SolutionA(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        _buffer = 0
        max_time = 0
        time_table = []
        key_table = []
        for i in range(len(releaseTimes)):
            if i == 0: _buffer = releaseTimes[i]
            else: _buffer = releaseTimes[i] - releaseTimes[i-1]
                
            if _buffer >= max_time:
                max_time =  _buffer
                time_table.append(max_time)
                key_table.append(keysPressed[i])
                
        #for i in range(len(time_table)):print(time_table[i],key_table[i])
        
        counter = len(time_table) - 1
        max_time = time_table[counter]
        _buffer = 0 
        res = key_table[counter]
        while(counter >= 0):
            if time_table[counter] < max_time: break 
            #print(counter,time_table[counter],key_table[counter])
            _buffer = key_table[counter]
            #print(ord(_buffer) , ord(res))
            if ord(_buffer) > ord(res): 
                #print(_buffer)
                res = _buffer
            counter = counter -1
        return res

if __name__ == "__main__":
    tester = SolutionA()
    