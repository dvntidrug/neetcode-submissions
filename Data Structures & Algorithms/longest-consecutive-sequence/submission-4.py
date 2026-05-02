class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums :
            num_set = set(nums)
            count = 1
            maxcount = 0 
            for i in nums : 
                if (i-1) in num_set : 
                    continue 
                else : 
                    while i+1 in num_set : 
                        i=i+1 
                        count = count + 1      
                    if count > maxcount : 
                        maxcount = count
                count = 1        
            return maxcount 
        else : 
            return 0

            

                

                