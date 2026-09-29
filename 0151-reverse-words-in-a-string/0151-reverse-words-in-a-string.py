class Solution(object):
    def reverseWords(self, s):
        l=0
        s=s.split()
        s=s[::-1]
        return " ".join(s)