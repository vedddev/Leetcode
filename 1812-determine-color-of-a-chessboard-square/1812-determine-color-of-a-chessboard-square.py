class Solution(object):
    def squareIsWhite(self, coordinates):
        mp={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        result=list(coordinates)
        ch=result[0]
        step=int(result[1])

        if mp[ch]%2==0 and step%2!=0:
            return True
        elif mp[ch]%2!=0 and step%2==0:
            return True
        return False
        