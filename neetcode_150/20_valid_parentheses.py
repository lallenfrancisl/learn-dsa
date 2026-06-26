class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack: list[str] = []

        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if len(stack) > 0 and brackets.get(stack[len(stack) - 1]) == char:
                    stack.pop()
                else:
                    stack.append(char)

        return len(stack) == 0
