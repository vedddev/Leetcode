class Solution(object):
    def largestInteger(self, nums, k):
        mp={}
        for i in range(len(nums) - k + 1):
            win=set()
            for j in range(i,i+k):
                win.add(nums[j])
                
            for num in win:
                if num in mp:
                    mp[num]+=1
                else:
                    mp[num]=1

        max_value=-1
        for i in nums:
            if mp[i]==1:
                max_value = max(max_value, i)
        return max_value

        