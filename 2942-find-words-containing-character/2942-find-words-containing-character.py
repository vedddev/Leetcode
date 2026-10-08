class Solution(object):
    def findWordsContaining(self, words, x):
        result=[]
        for word in range(len(words)):
            for ch in words[word]:
                if ch==x:
                    result.append(word)
                    break
        return result
        