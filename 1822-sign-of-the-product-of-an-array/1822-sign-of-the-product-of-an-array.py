class Solution(object):
    def arraySign(self, nums):
        mul=1

        for i in nums:
            mul*=i
        if mul>0:
            return 1
        elif mul<0:
            return -1
        else:
            return 0
        