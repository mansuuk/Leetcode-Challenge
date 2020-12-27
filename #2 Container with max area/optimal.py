class Solution:
    def maxArea(self, arr: List[int]) -> int:
        maxA = 0
        i = 0
        j = len(arr)-1
        while i<j:
            while j>i:
                maxA = max((min(arr[i], arr[j])*(j-i)), maxA)
                if arr[i]<arr[j]:
                    i+=1
                else:
                    j-=1
        return maxA
                    
        
