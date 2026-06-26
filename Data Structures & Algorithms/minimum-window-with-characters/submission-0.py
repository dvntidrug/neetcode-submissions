class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : 
            return ""
        else : 
            leftpointer = 0 
            formed = 0
            need = {}
            window = {}
            best = (0,0)
            bestlen = len(s)+1
            for i in t :
                if i not in need :
                    need[i] = 1 
                else : 
                    need[i] += 1 
            
            
            required = len(need)

            for rightpointer in range(len(s)) :
                if s[rightpointer] in need :
                    if s[rightpointer] not in window :
                        window[s[rightpointer]] = 1 
                    else : 
                        window[s[rightpointer]] += 1 
                
                    c = s[rightpointer] 
                    if window[c] == need[c] : 
                        formed += 1
                
                while formed == required :
                    currentlength = rightpointer - leftpointer +1
                    if currentlength < bestlen:
                        best = (leftpointer,rightpointer)
                        bestlen = currentlength 


                    if s[leftpointer] in need : 
                        if s[leftpointer] in window : 
                            window[s[leftpointer]] -=1
                            
                            if window[s[leftpointer]] < need[s[leftpointer]] :
                                formed -=1
                    leftpointer+=1
            
            if bestlen == len(s) + 1:
                return ""

            return s[best[0] : best[1] + 1]

