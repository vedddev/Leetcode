class Solution(object):
    def compress(self, chars):
        count=1
        result=[]
        for i in range(1,len(chars)):
            if chars[i-1]==chars[i]:
                count+=1
            else:
                result.append(chars[i-1])
                if count>1:
                    result.extend(list(str(count)))
                count=1
            
        result.append(chars[-1])
        if count>1:
                result.extend(list(str(count)))
        chars[:]=result
            
        return len(chars)
        