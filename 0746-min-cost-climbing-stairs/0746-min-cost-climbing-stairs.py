class Solution(object):
    def minCostClimbingStairs(self, cost):
        prev=0
        prev2=0

        for i in range(1,len(cost)):
            curr=min(prev2+cost[i-1],prev+cost[i])
            prev2=prev
            prev=curr
        return prev
        