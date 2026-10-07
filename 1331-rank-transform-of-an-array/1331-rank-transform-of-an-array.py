class Solution(object):
    def arrayRankTransform(self, arr):
        nums=sorted(list(set(arr)))
        mp={}
        l=1
        for i in nums:
            mp[i]=l
            l+=1
        result=[]
        for i in arr:
            result.append(mp[i])
        return result
        