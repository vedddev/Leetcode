class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums=sorted(nums)
        l=0
        r=len(nums)-1
        avg=0
        result=[]
        while l<r:
            avg=nums[l]+nums[r]
            avg/=2
            result.append(avg)
            l+=1
            r-=1
        min_value=result[0]
        for i in range(1,len(result)):
            if min_value>result[i]:
                min_value=result[i]
        return min_value