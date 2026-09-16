class Solution(object):
    def limitOccurrences(self, nums, k):
        l=0
        for r in range(len(nums)):
           if l<k or nums[r]!=nums[l-k]:
            nums[l]=nums[r]
            l+=1
        return nums[:l]
        