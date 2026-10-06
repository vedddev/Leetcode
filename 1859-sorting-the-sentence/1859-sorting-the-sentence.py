class Solution(object):
    def sortSentence(self, s):
        s=s.split()
        result=sorted(s,key=lambda x: x[-1])
        print(result)
        text=[]
        for i in range(len(result)):
            text.append(result[i][0:len(result[i])-1])
        return " ".join(text)



        
        