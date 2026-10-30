class Solution(object):
    def separateDigits(self, nums):
        result=""
        for i in nums:
            result+=str(i)
        
        s=list(result)
        result1=[]
        for i in s:
            result1.append(int(i))
        return result1
        