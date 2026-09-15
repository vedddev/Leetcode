class Solution(object):
    def firstPalindrome(self, words):
        
        for word in words:
            l=0
            r=len(word)-1
            if len(word)==1:
                return word
            while(l<r):
                if word[l]!=word[r]:
                    break
                l+=1
                r-=1
                if l>=r:
                    return word
        return ""
        