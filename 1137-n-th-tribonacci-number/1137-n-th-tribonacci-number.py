class Solution(object):
    def tribonacci(self, n):
        prev=0
        prev2=1
        prev3=1
        if n==0:
            return 0
        for i in range(3,n+1):
            curr=prev+prev2+prev3
            prev=prev2
            prev2=prev3
            prev3=curr
        return prev3
        
        