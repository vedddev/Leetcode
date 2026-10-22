class Solution(object):
    def halvesAreAlike(self, s):
        st,end=0,len(s)-1
        mid=(st+end)//2
        word1=s[:mid+1]
        word2=s[mid+1:end+1]
        count1=0
        count2=0

        for i in word1:
            if i in "aeiouAEIOU":
                count1+=1
        for i in word2:
            if i in "aeiouAEIOU":
                count2+=1
        if count1==count2:
            return True
        return False

        

        