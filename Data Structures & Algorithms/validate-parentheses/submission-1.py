class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        pairs = {')':'(',']':'[','}':'{'}
        for i in s : 
            if i == ")" or i == "]" or i == "}" :
                if not stack :
                    return False 
                else : 
                    if pairs[i] == stack[-1] : 
                        stack.pop()
                    else : 
                        return False         
            else : 
                stack.append(i)
        
        if not stack : 
            return True 
        else : 
            return False 



