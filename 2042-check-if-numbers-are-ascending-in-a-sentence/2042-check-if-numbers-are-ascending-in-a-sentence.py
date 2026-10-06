class Solution(object):
    def areNumbersAscending(self, s):
        result=[]
        
        for i in s.split():
           if i.isdigit():
            result.append(int(i))
        print(result)
        
        l=0
        for i in range(1,len(result)):
            if result[i]<=result[l]:
                return False
            l+=1
        return True
        
