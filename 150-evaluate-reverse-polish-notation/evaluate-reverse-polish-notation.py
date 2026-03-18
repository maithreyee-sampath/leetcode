import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+","-","/","*"}
        def eval(op,a,b):
            if op == "+":
                return a+b
            elif op == "-":
                return a-b
            elif op == "*":
                return a*b
            elif op == "/":
                return math.floor(a/b) if a/b > 0 else math.ceil(a/b)
        
        stack = []
        for val in tokens:
            
            if val in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(eval(val,a,b))
            else:
                stack.append(int(val))

                    
        return stack[0]