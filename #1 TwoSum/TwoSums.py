def twoSum(nums, target):
    hashMap = {}
    for i in range(len(nums)):
        numToFind = target - nums[i]
        if numToFind in hashMap:
            return(i, hashMap[numToFind])
        else:
            hashMap[nums[i]] = i
    return []
        
        
