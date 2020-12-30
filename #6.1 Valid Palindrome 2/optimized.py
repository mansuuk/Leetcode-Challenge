class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(start, end):
            while start < end and s[start] == s[end]:
                start += 1            
                end -= 1
            return start >= end, start, end
        found, i, j = isPalindrome(0, len(s) - 1)        
        # Just palindrom without any delete
        if found:
            return True
        # Remove s[i] case
        newI, newJ = i + 1, j
        found, newI, newJ = isPalindrome(i + 1, j)
        if found:
            return True
        # Remove s[j] case
        found, newI, newJ = isPalindrome(i, j - 1)    
        if found:
            return True
        # Cannot find in both cases
        return False
            
    
    
        
        
