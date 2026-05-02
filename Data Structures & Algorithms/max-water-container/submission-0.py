class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftpointer = 0
        rightpointer = len(heights)-1
        currentarea = 0 
        maxarea = 0 
        while leftpointer < rightpointer  : 
            currentarea = (rightpointer - leftpointer) * min(heights[rightpointer],heights[leftpointer])
            if currentarea > maxarea : 
                maxarea = currentarea 
            if heights[leftpointer] < heights[rightpointer]:
                leftpointer += 1 
            elif heights[rightpointer] < heights[leftpointer]:
                rightpointer -= 1 
            elif heights[rightpointer] == heights[leftpointer] :
                rightpointer -= 1 


        return maxarea 

            
            
