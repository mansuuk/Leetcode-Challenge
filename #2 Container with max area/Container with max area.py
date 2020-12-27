#https://leetcode.com/problems/container-with-most-water/
#Brute force O(n^2)
#Rejected by Leetcode
def maxArea(arr):
    maxA = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            maxA = max((min(arr[i], arr[j])*(j-i)), maxA)
    return maxA
