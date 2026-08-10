class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = "{[("
        for b in s:
            if b in opening:
                stack.append(b)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (b == "]" and top != "[") or (b == ")" and top != "(") or (b == "}" and top != "{"):
                    return False
        if not stack:
            return True
        else:
            return False
                    