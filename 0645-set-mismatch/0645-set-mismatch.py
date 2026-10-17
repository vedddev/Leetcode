class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        mp={}
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]]+=1
                result.append(nums[i])
            else:
                mp[nums[i]]=1
        for i in range(1,len(nums)+1):
            if i not in mp:
                result.append(i)
        return result