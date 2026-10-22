class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums=sorted(nums1+nums2)
        st=0
        end=len(nums)-1
        for i in range(len(nums)):
            mid=(st+end)//2
            if len(nums)%2!=0:
                return nums[mid]
            else:
                return (nums[mid]+nums[mid+1])/2