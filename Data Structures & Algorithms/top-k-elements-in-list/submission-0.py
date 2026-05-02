class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mynumdict={}
        for i in nums : 
            if i not in mynumdict : 
                mynumdict[i]= 1 
            else : 
                mynumdict[i] += 1 

        numfreq = list(mynumdict.items()) 
        sortedpairs = sorted(numfreq,key=lambda x: x[1] , reverse = True)
        numlist = [x[0]for x in sortedpairs]  
        result = numlist[:k]
        return result 

        