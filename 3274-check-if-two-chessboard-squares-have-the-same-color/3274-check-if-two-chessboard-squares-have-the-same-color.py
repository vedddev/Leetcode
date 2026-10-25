class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        mp={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        c1=mp[coordinate1[0]]
        r1=int(coordinate1[1])
        c2=mp[coordinate2[0]]
        r2=int(coordinate2[1])

        color1=(c1+r1)%2
        color2=(c2+r2)%2

        return color1==color2
        
        