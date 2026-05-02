class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs :  
            s += str(len(i))+ '#' + i
        return s 

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0 
        while i < len(s) : 
            pos = s.find('#',i) 
            length = int(s[i:pos]) 
            i = pos + 1 
            substring = s[i:i+length]
            decoded.append(substring)
            i = i + length 
        return decoded 
