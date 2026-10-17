class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mp1={}
        mp2={}
        r=list(ransomNote)
        m=list(magazine)
        
        for i in r:
            if i in mp1:
                mp1[i]+=1
            else:
                mp1[i]=1

        for i in m:
            if i in mp2:
                mp2[i]+=1
            else:
                mp2[i]=1

        for i,j in mp1.items():
            if i not in mp2 or mp2[i]<j:
                return False
        return True