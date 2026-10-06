class Solution(object):
    def finalValueAfterOperations(self, operations):
        mp={
            "X++":1,
            "--X":-1,
            "++X":1,
            "X--":-1
            }
        sum=0
        for i in operations:
            sum+=mp[i]
        
        return sum