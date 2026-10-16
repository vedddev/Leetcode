class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        p=re.sub(r'[^a-zA-Z\s]', ' ', paragraph)
        p=p.split()
        mp={}
        for i in range(len(p)):
            if p[i] in mp:
                mp[p[i]]+=1
            else:
                mp[p[i]]=1
        
        banned = set(banned)
        result=""
        count=0

        for i,j in mp.items():
            if i not in banned and j>count:
                count=j
                result=i
        return result        
        