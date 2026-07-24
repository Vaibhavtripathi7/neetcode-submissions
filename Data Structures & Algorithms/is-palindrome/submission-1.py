class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer method: 
        i = 0
        j = len(s) - 1
        
        while i < j: 
            if (s[i]== " " or s[i] == "?"):
                i += 1 
            elif (s[j] == " " or s[j] == "?"):
                j -= 1
            elif (s[i].lower() == s[j].lower()):
                i += 1
                j -= 1
            else: 
                return False 
        return True 
