class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(int(t)) # [1, 2] "+"
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                match t:
                    case "+":
                        res = op1+op2
                    case "-":
                        res = op1-op2
                    case "*":
                        res = op1*op2
                    case "/":
                        res = int(op1/op2)
                
                stack.append(res)

        return int(stack[0])
                    

