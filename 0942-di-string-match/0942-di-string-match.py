class Solution(object):
    def diStringMatch(self, s):
        n1=len(s)
        n2=0
        result=[]
        for i in range(len(s)):
            if s[i]=="I":
                result.append(n2)
                n2+=1
            elif s[i]=="D":
                result.append(n1)
                n1-=1
        result.append(n1)
        return result

        