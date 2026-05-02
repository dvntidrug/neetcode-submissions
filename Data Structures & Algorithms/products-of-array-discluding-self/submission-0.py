class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodleft = 1
        prodright = 1
        leftpass = []
        rightpass = []
        result = []
        for i in range(len(nums)) : 
            leftpass.append(prodleft)
            prodleft  = prodleft * nums[i] 

        for i in range(len(nums)-1,-1,-1):
            rightpass.append(prodright) 
            prodright = prodright * nums[i] 
        rightpass.reverse()

        for i in range(len(rightpass)): 
            result.append(leftpass[i]*rightpass[i])
            
        return result 


        