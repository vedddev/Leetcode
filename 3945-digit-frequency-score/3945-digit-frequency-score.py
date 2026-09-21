class Solution(object):
    def digitFrequencyScore(self, n):

        mp={}
        while n>0:
            digit=n%10
            if digit in mp:
                mp[digit]+=1
            else:
                mp[digit]=1
            n//=10

        sum=0
        for i,j in mp.items():
            mul=i*j
            sum+=mul
        return sum
        