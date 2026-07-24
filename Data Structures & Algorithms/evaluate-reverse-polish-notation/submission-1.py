class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-','/', '*'] 
        for i in tokens:
            if i in operators: 
                if (i == '+'):
                    a = stack.pop()
                    b = stack.pop()
                    c = int(b) + int(a) 
                    stack.append(c)

                if (i == '-'):
                    a = stack.pop()
                    b = stack.pop()
                    c = int(b) - int(a) 
                    stack.append(c)
                if (i == '*'):
                    a = stack.pop()
                    b = stack.pop()
                    c = int(b) * int(a) 
                    stack.append(c)
                if (i == '/'):
                    a = stack.pop()
                    b = stack.pop()
                    c = int(b) / int(a) 
                    stack.append(c)
            else: 
                stack.append(i)
        return stack[-1]