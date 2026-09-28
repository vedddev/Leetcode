class Solution(object):
    def shortestToChar(self, s, c):
        
        index1=[]
        result=[]
        for i in range(len(s)):
            if c==s[i]:
                index1.append(i)
        n=0
        for i in range(len(s)):
            distance=float('inf')

            for j in index1:
                distance=min(distance,abs(i-j))

            result.append(distance)
        return result
        