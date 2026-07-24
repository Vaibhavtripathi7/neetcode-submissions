class Solution:
    def isValid(self, s: str) -> bool:
        # using hashing can solve it: 
        # but have to try stack: first in -- last out !
        # stack -- list
        
        stack = []

        for i in s: 
            a = len(stack) - 1
            if a == -1:
                a = 1
                
            if ( i == ']'):
                if (stack and stack[a] == '['):
                    stack.pop()
                    continue 
            elif( i == '}'):
                if stack and stack[a] == '{':
                    stack.pop()
                    continue 

            elif( i == ')'):
                if (stack and stack[a] == '('):
                    stack.pop()
                    continue

            stack.append(i)
        if (len(stack) == 0):
            return True
        else: 
            return False


