# Leetcode-Challenge
This repository contains 30 coding challenges covering various DSA concepts and gotchas.

1. Two Sum: https://leetcode.com/problems/two-sum/
	- Use a hashmap hash[arr[i]] = i

2. Container with most water: https://leetcode.com/problems/container-with-most-water/
	-Don't confuse this with trapping rainwater problem.
	-Volumes of walls are negligible so, a wall between two walls doesnt matter.
    	-Water between walls at indices i and j = min(arr[i], arr[j])*(j-i)
    	-Start with the two pointers away from each other ie i=0, j=len(arr). Move the pointer which has the minimum element.

3. Trapping Rainwater: https://leetcode.com/problems/trapping-rain-water/
    	-Water at each index can be found in isolation.
	-Water at i = min(maxL, maxR) - arr[i]. maxL = max(arr[:i]); maxR = max(arr[i+1:]).
  
 
