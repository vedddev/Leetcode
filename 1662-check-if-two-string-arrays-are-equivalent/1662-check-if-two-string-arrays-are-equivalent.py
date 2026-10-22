class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        wordA=""
        wordB=""
        for i in word1:
            wordA+=i
        for i in word2:
            wordB+=i
        if wordA==wordB:
            return True
        return False
        