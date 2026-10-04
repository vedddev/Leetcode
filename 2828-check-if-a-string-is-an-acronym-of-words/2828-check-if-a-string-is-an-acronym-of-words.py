class Solution(object):
    def isAcronym(self, words, s):
        store=[]
        for word in words:
            store.append(word[0])
        
        store="".join(store)
        if store==s:
            return True
        return False

        