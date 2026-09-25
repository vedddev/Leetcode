class Solution(object):
    def getCommon(self, nums1, nums2):
        s1=set(nums1)
        s2=set(nums2)
        nums=list(s1&s2)
        if len(nums)==0:
            return -1
        min_value=float('inf')
        for i in range(len(nums)):
            if min_value>nums[i]:
                min_value=nums[i]

        return min_value
        
