class Solution(object):
    def firstPalindrome(self, words):
        result=[]
        for word in words:
            if word==word[::-1]:
                return word
        return ""
        