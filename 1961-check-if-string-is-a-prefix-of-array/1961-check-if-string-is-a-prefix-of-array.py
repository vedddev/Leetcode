class Solution(object):
    def isPrefixString(self, s, words):
        s1=""
        for word in words:
            s1+=word

            if s1==s:
                return True
            
            if len(s1)>len(s):
                return False
        return False
        