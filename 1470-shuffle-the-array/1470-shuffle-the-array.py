class Solution(object):
    def shuffle(self, nums, n):
        x=[]
        y=[]
        for i in range(len(nums)):
            if i>n-1:
                y.append(nums[i])
            else:
                x.append(nums[i])
        X_Y=[]
        l=0
        while l<len(x) and l<len(y):
            X_Y.append(x[l])
            X_Y.append(y[l])
            l+=1
        return X_Y
        