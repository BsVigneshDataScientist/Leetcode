# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:

''' need to revisit the logic is chatgpt '''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        stack = []
        output = []

        for ch in s:

            if ch == '(':
                if stack:
                    output.append(ch)
                stack.append(ch)

            else:
                stack.pop()
                if stack:
                    output.append(ch)

        return ''.join(output)
        