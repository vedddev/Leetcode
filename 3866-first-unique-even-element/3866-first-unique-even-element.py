class Solution(object):
    def firstUniqueEven(self, nums):
        mp={}
        for i in nums:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        for i in nums:
            if i % 2 == 0 and mp[i] == 1:
                return i
        return -1
        