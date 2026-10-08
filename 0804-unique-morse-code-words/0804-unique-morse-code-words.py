class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse_code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        l=1
        char=[]
        for i in range(ord('a'),ord('z')+1):
            char.append(chr(i))
        
        mp=dict(zip(char,morse_code))
        result=[]
        for word in words:
            mose=""
            for ch in word:
                mose+=mp[ch]
            
            result.append(mose)
        return len(set(result))

        