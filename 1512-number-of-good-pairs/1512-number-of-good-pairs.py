class Solution(object):
    def numIdenticalPairs(self, nums):
        mp={}
        count=0
        for i in nums:
            if i in mp:
                count+=mp[i]
                mp[i]+=1
            else:
                mp[i]=1
        return count
        