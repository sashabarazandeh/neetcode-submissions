class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "*+-/"
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:

                n2 = stack.pop()
                n1 = stack.pop()
                result = 0
                if t == "*":
                    result = n1 * n2
                elif t == "+":
                    result = n1 + n2    
                elif t == "-":
                    result = n1 - n2
                elif t == "/":
                    result = int(n1 / n2)
                stack.append(result)
        ans = stack.pop()
        return int(ans)
