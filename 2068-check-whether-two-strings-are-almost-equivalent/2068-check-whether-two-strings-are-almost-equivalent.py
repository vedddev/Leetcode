class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        mp1={}
        mp2={}
        for i in word1:
            if i in mp1:
                mp1[i]+=1
            else:
                mp1[i]=1
        for i in word2:
            if i in mp2:
                mp2[i]+=1
            else:
                mp2[i]=1
        for i in range(ord('a'), ord('z') + 1):
            ch = chr(i)
            if abs(mp1.get(ch, 0) - mp2.get(ch, 0)) > 3:
                return False

        return True
    