class Solution(object):
    def countKDifference(self, nums, k):
        mp={}
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                diff=abs(nums[i]-nums[j])
                if diff==k:
                    count+=1
        return count
        