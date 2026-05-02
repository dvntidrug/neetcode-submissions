class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortednums = sorted(nums)
        triplet = []              
        for i in range(len(sortednums)) :
            j = i+1 
            k = len(sortednums)-1 
            if i>0 and sortednums[i] == sortednums[i-1] : 
                continue 
            else :  
                a = sortednums[i]
                target = -a 
                while j < k : 
                    if sortednums[j] + sortednums[k] < target  : 
                        j=j+1 
                    elif sortednums[j] + sortednums[k] > target :
                        k = k-1 
                    elif sortednums[j]+ sortednums[k] == target : 
                        triplet.append([a,sortednums[j],sortednums[k]])
                        j = j+1 
                        k = k-1
                        while j < k and sortednums[j] == sortednums[j-1] :
                            j= j+1 
                        while j < k and sortednums[k] == sortednums[k+1] :
                            k= k-1  
        return triplet                
                    