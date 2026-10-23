class Solution(object):
    def getRow(self, rowIndex):
        result=[]
        if rowIndex==0:
            return [1]
        for i in range(1,rowIndex+2):
            result.append([1]*i)
        for i in range(1,len(result)):
            for j in range(1,len(result[i])-1):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
            if i==rowIndex:
                return result[i]
        