class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer method: 
        i = 0
        j = len(s) - 1
        
        while i < j: 
            if not s[i].isalnum():
                i += 1 
            elif not s[j].isalnum():
                j -= 1
            elif (s[i].lower() == s[j].lower()):
                i += 1
                j -= 1
            else: 
                return False 
        return True 
