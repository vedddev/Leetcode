class Solution(object):
    def wordPattern(self, pattern, s):
        
        pattern=list(pattern)
        s=s.split()
        if len(pattern) != len(s):
            return False
        mp1={}
        mp2={}
        for i in range(len(pattern)):
            ch=pattern[i]
            word=s[i]
            if ch in mp1:
                if mp1[ch]!=word:
                    return False
            else:
                mp1[ch]=word
            
            if word in mp2:
                if mp2[word]!=ch:
                    return False
            else:
                mp2[word]=ch
        return True

            
        