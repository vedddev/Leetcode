class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count=0

        for word in words:
            allowed=set(allowed)
            con=True
            for ch in word:
                if ch not in allowed:
                    con=False
                    break
                    
            if con:
                count+=1
        return count
        