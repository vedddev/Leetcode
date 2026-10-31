class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        count=0
        for i in details:
            s=int(i[11:13])

            if s>60:
                print(s)
                count+=1
        return count
        