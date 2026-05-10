class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(first,second,operator):
            if operator == '+':
                return first + second
            elif operator == '-':
                return first - second
            elif operator == '*':
                return first * second
            else:
                return int(first/second)
        operators = ['+','-','*','/']
        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                print(t, stack)
                second = stack.pop()
                first = stack.pop()
                result = operate(first, second, t)
                stack.append(result)
        
        return stack.pop()

        