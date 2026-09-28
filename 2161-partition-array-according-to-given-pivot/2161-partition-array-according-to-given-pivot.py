class Solution(object):
    def pivotArray(self, nums, pivot):
        re=[]
        su=[]
        lt=[]
        for i in nums:
            if i<pivot:
                re.append(i)
            elif i==pivot:
                su.append(i)
            else:
                lt.append(i)
        result=re+su+lt
        return result
    
            