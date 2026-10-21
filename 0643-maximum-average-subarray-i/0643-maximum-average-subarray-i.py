class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum=sum(nums[:k])
        max_sum=window_sum
        for r in range(k,len(nums)):
            window_sum-=nums[r-k]
            window_sum+=nums[r]

            max_sum=max(window_sum,max_sum)

        return max_sum/k
