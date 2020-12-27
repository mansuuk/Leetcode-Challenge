def trapRain(arr):
    i = 0
    fullVol = 0
    j=0
    while i < len(arr)-1:
        if arr[i]==0:
            i+=1
        
        else:
            j = i+1
            currVol = 0
            while arr[j]<arr[i]:
                currVol += arr[i]-arr[j]
            fullVol += currVol
            j += 1
        i=j
    return fullVol
