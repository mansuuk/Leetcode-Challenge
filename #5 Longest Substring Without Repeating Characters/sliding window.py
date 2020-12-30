class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        hashmap = {}
        i = 0
        for j in range(n):
            if s[j] in hashmap:
                i = max(hashmap[s[j]], i)
            ans = max(ans, j-i+1)
            hashmap[s[j]] = j+1
        return ans
                
            
