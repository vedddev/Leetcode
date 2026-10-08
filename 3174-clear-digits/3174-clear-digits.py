class Solution(object):
    def clearDigits(self, s):
        st=[]
        for i in s:
            if i.isdigit():
                st.pop()
            else:
                st+=i
        return "".join(st)
        