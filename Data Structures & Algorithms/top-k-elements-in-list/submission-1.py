class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        result = []
        for i in nums : 
            if i not in mydict : 
                mydict[i] = 1 
            else : 
                mydict[i] += 1 

        bucket = [[]for _ in range(len(nums)+1)]        
        for num in mydict : 
            bucket[mydict[num]].append(num)
        for i in range(len(bucket)-1,0,-1):
            for j in range (len(bucket[i])): 
                result.append(bucket[i][j])
            if len(result) == k : 
                return result 