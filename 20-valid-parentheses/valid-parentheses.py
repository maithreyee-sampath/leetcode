class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(","}":"{","]":"["}
        stack = []

        for i in range(len(s)):
            if s[i] in brackets.values(): #if its an opening bracket
                stack.append(s[i])
            elif s[i] in brackets.keys():
                if not stack or stack[-1] != brackets[s[i]]:
                    return False
                stack.pop()

        return len(stack) == 0

            