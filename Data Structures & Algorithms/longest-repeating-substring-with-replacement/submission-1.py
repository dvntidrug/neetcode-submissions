class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        win_length = 0
        max_length = 0  
        leftpointer = 0 
        freq = {}
        for rightpointer in range(len(s)) : 
            if s[rightpointer] not in freq : 
                freq[s[rightpointer]] = 1 
            else : 
                freq[s[rightpointer]] +=1

            maxfreq = max(freq.values())
            win_length = rightpointer - leftpointer + 1

            if  win_length - maxfreq <= k :
                if win_length > max_length : 
                    max_length = win_length
            else : 
                while win_length - maxfreq > k :
                        freq[s[leftpointer]] -= 1
                        leftpointer +=1 
                        win_length -= 1 
                        maxfreq = max(freq.values())

        return max_length 
          


