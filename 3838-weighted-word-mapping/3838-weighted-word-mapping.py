class Solution(object):
    def mapWordWeights(self, words, weights):
        mp1 = {}
        mp2 = {}

        for i in range(26):
            ch = chr(ord('a') + i)
            mp1[ch] = weights[i]
            mp2[i] = ch
        
        word1=""
        for word in words:
            sum=0
            for ch in word:
                sum+=mp1[ch]
            modulo=sum%26
            word1+=mp2[25-modulo]
        return word1



        
            