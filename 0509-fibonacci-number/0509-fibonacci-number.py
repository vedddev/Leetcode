class Solution(object):
    def fib(self, n):
        prev=0
        prev2=1
        for i in range(n):
            curri=prev+prev2
            prev2=prev
            prev=curri
        return prev
        