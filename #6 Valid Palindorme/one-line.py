class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(x for x in s if x.isalnum()).lower()
        return st==st[::-1]
        
