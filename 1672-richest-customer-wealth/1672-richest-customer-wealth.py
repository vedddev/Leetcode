class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_sum=0
        result=[]
        for i in range(len(accounts)):
            result.append(sum(accounts[i]))
        return max(result)


        