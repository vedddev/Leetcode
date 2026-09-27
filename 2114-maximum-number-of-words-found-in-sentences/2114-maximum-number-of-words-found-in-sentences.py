class Solution(object):
    def mostWordsFound(self, sentences):
        maxlen=0
        for i in range(len(sentences)):
            result=sentences[i].split()
            maxlen=max(maxlen,len(result))
        return maxlen
    