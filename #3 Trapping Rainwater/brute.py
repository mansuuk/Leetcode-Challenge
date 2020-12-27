def trapRain(arr):
    water = 0
    for i in range(len(arr)-1):
        maxL = max(arr[:i] if arr[:i] else [0])
        maxR = max(arr[i+1:] if arr[i+1:] else [0])
        waterAti = min(maxL, maxR) - arr[i]
        if waterAti>0:
            water += waterAti
    return water
