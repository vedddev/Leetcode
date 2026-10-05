class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        mp={}
        for i in stones:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        sum=0
        for i in range(len(jewels)):
            if jewels[i] in mp:
                sum+=mp[jewels[i]]
        return sum
        