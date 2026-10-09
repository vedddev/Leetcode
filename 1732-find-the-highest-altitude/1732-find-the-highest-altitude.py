class Solution(object):
    def largestAltitude(self, gain):
        result=[]
        n=0
        result.append(0)
        for i in gain:
            res=n-i
            n=res
            result.append(-res)
        max_value=0
        for i in result:
            if i>max_value:
                max_value=i
        return max_value

        