class Solution(object):
    def isBalanced(self, num):
        nums=[]
        for i in num:
            nums.append(int(i))
        
        odd_sum=0
        even_sum=0
        for i in range(len(nums)):
            if i%2==0:
                even_sum+=nums[i]
            else:
                odd_sum+=nums[i]
        if odd_sum==even_sum:
            return True
        return False
        