class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+-*/':
                a, b = stack.pop(), stack.pop() 
                if (i == '+'):
                    c = int(b) + int(a) 
                    stack.append(c)
                elif (i == '-'):
                    c = int(b) - int(a) 
                    stack.append(c)
                elif (i == '*'):
                    c = int(b) * int(a) 
                    stack.append(c)
                else :
                    c = int(b) / int(a) 
                    stack.append(c)
            else: 
                stack.append(i)
        
        return int(stack[0])