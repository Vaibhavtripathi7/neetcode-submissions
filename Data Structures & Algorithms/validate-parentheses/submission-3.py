class Solution:
    def isValid(self, s: str) -> bool:
        # using hashing can solve it: 
        # but have to try stack: first in -- last out !
        # stack -- list
        
        stack = []

        for i in s: 
                
            if ( i == ']'):
                if (stack and stack[-1] == '['):
                    stack.pop()
                    continue 
            elif( i == '}'):
                if stack and stack[-1] == '{':
                    stack.pop()
                    continue 

            elif( i == ')'):
                if (stack and stack[-1] == '('):
                    stack.pop()
                    continue

            stack.append(i)
        if (len(stack) == 0):
            return True
        else: 
            return False


