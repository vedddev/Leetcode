class Solution(object):
    def interpret(self, command):
        word=""
        for i in range(len(command)):
            if command[i]=='G':
                word+="G"
            if command[i-1]=="(" and command[i]==")":
                word+="o"
            if command[i-1]=="(" and command[i]=="a":
                word+="al"
        return word
        