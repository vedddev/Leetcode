class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mp={}
        for i in nums:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        count_pairs=0
        remain=0
        result=[]
        for i,j in mp.items():
            count_pairs+=j//2
            remain+=j%2
        result.append(count_pairs)
        result.append(remain)
        return result