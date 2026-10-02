class Solution(object):
    def replaceDigits(self, s):
        store=[]
        for i in range(len(s)):
            if s[i].isalpha():
                store.append(s[i])
            else:
                ch = chr(ord(s[i-1]) + int(s[i]))
                store.append(ch)
        return "".join(store)