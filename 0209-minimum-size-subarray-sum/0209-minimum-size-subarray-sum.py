class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        min_len=float('inf')
        sum=0
        for r in range(len(nums)):
            sum+=nums[r]
            
            while target<=sum:
                min_len=min(min_len,r-l+1)
                sum-=nums[l]
                l+=1
        if min_len==float('inf'):
                return 0

        return min_len
        