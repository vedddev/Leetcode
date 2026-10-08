class Solution(object):
    def maxFreqSum(self, s):
        vowls=['a', 'e', 'i', 'o','u']

        mp={}
        for char in s:
            if char in mp:
                mp[char]+=1
            else:
                mp[char]=1
        max_vowls=0
        max_consonants=0
        for i,j in mp.items():
            if i in vowls:
                max_vowls=max(max_vowls,j)
            else:
                max_consonants=max(max_consonants,j)
        return max_vowls+max_consonants