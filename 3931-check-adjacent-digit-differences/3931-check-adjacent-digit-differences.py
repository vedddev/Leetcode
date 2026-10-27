class Solution(object):
    def isAdjacentDiffAtMostTwo(self, s):
        s=list(s)
        
        for i in range(1,len(s)):
            sub=int(s[i])-int(s[i-1])
            print(sub)
            if abs(sub)>2:
                return False
        return True