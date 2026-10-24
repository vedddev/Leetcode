class Solution(object):
    def maxPower(self, s):
        count=1
        max_count=0
        if len(s)==1:
            return 1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                count=1
            max_count=max(max_count,count)
        return max_count
        