class Solution:
    def isValid(self, s: str) -> bool:
        # using hashing can solve it: 
        # but have to try stack: first in -- last out !
        # stack -- list
        
        stack = []
        pairs = {']': '[', '}': '{', ')': '('}

        for char in s:
            if char in pairs:
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if (len(stack) == 0):
            return True
        else: 
            return False


