class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"}":"{","]":"[",")":"("}
        stack = []
        for character in s:
            if character in bracket_map:
                if stack and stack[-1] == bracket_map[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
        return not stack

        