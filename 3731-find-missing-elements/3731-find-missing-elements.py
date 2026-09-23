class Solution(object):
    def findMissingElements(self, nums):
        s=set(nums)
        maxNum=max(nums)
        minNum=min(nums)
        result=[]
        for i in range(minNum,maxNum):
            if i not in s:
                result.append(i)
        return result
        
        