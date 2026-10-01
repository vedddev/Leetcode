class Solution(object):
    def scoreOfString(self, s):
        mp = {chr(i): i for i in range(97, 123)}
        ls=[]
        for i in s:
            ls.append(i)
        
        sum=0
        l=0
        r=l+1
        while r<len(s):
            sub=0
            sub=abs(mp[ls[l]]-mp[ls[r]])
            sum+=sub
            l+=1
            r+=1
        return sum   