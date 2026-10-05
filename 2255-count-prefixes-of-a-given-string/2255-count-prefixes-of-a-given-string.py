class Solution(object):
    def countPrefixes(self, words, s):
        count=0
        for word in words:
            if s[0:len(word)] == word:
                count+=1
        return count