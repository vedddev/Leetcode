class Solution(object):
    def generate(self, numRows):
        result=[]
        for i in range(1,numRows+1):
            result.append([1]*i)
        print(result)
        for i in range(1,len(result)):
            for j in range(1,len(result[i])-1):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result
