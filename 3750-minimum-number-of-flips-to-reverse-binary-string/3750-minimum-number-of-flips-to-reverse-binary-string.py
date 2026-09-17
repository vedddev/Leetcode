class Solution(object):
    def minimumFlips(self, n):
        s=format(n,"b")
        s=list(s)
        l=0
        r=len(s)-1
        count=0
        s=s[::-1]
        while l<r:
            if s[r]!=s[l]:
                count+=1
            l+=1
            r-=1
        return count*2
        
        
        