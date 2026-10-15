class Solution(object):
    def sumDivisibleByK(self, nums, k):
        mp={}
        for i in nums:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        sum=0
        for i,j in mp.items():
            if j%k==0:
                sum+=i*j
        return sum
        