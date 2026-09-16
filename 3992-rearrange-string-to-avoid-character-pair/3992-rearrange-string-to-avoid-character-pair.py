class Solution(object):
    def rearrangeString(self, s, x, y):
        s1=[]
        for ch in s:
           if ch != x and ch != y:
                s1.append(ch)
        return y*s.count(y)+"".join(s1)+x*s.count(x)
        