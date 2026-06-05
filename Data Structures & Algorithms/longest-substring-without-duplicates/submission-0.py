class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0  
        maximum = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set: 
                char_set.remove(s[left])
                left = left + 1 
            else : 
                char_set.add(s[right])
                length = right - left + 1
            
            if length > maximum: 
                maximum = length 
    
        return maximum 
