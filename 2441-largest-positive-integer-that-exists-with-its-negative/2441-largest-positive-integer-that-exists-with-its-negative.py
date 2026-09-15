class Solution(object):
    def findMaxK(self, nums):
        mp=set(nums)
        result=-1
        for i in nums:
            if i>result and -i in mp:
                result=max(result,i)
        return result
        