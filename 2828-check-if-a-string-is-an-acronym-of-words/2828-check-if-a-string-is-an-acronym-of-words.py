class Solution(object):
    def isAcronym(self, words, s):
        store=""
        for word in words:
            store+=word[0]
        
        if store==s:
            return True
        return False

        