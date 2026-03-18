class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(","}":"{","]":"["}
        stack = []

        for i in range(len(s)):
            if s[i] in brackets.keys() and not stack:
                return False
            elif s[i] in brackets.keys() and stack[-1] != brackets[s[i]]:
                return False
            elif s[i] in brackets.keys() and stack[-1] == brackets[s[i]]:
                stack.pop()
            elif s[i] in brackets.values():
                stack.append(s[i])

        if stack:
            return False
        else:
            return True