class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums=sorted(nums)
        l=0
        r=len(nums)-1
        min_value=float('inf')
        while l<r:
            avg=(nums[l]+nums[r])/2
            min_value=min(min_value,avg)
            l+=1
            r-=1
        return min_value