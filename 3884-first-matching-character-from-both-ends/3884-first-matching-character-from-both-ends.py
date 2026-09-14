class Solution(object):
    def firstMatchingIndex(self, s):
        s=list(s)
        l=0
        r=len(s)-1
        while(l<=r):
            if s[l]==s[r]:
                return l
            l+=1
            r-=1
        return -1
        
        