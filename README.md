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
	-Water at i = min(maxL, maxR) - arr[i]. maxL = max(arr[:i]); maxR = max(arr[i+1:]). (brute force)
	-Use two pointers at the start and the end resp, move the minimum pointer. Thses pointers are used to store the max value seen from either sides.
	-When a pointer is moved it stores the water holding capacity at that index.

4. Backspace String Compare: https://leetcode.com/problems/backspace-string-compare/
	-Use Stack.

5. Longest substring without repeating characters: https://leetcode.com/problems/longest-substring-without-repeating-characters/
	-Use sliding window with a hashmap(set)

6. Valid Palindrome: https://leetcode.com/problems/valid-palindrome/

6.1 Valid Palindrome 2: https://leetcode.com/problems/valid-palindrome-ii/
	-Use two converging pointers.
	-replace characters both at right and left index in different passes and verify if resulting string is a palindrome.
  
 
