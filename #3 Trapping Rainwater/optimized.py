class Solution:
    def trap(self, arr):
        water = 0
        if len(arr)<3:
            return water
        maxL = arr[0]
        maxR = arr[-1]
        i = 0
        j = len(arr)-1
        while j>=i:
            #maxL = max(arr[:i] if arr[:i] else [0])
            #maxR = max(arr[i+1:] if arr[i+1:] else [0])
            maxL = max(maxL, arr[i])
            maxR = max(maxR, arr[j])
            
            if maxL<maxR:
                waterAtp = maxL - arr[i]
                if waterAtp>0:
                    water += waterAtp
                i+=1
            else:
                waterAtp = maxR - arr[j]
                if waterAtp>0:
                    water += waterAtp
                j-=1
        return water
        
