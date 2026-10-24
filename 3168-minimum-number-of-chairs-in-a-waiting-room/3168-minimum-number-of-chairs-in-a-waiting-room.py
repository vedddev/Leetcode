class Solution(object):
    def minimumChairs(self, s):
        count=0
        max_count=0

        for i in range(len(s)):
            if s[i]=="E":
                count+=1
            else:
                count-=1
            max_count=max(max_count,count)
        return max_count
        