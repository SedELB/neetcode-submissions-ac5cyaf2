class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = { ")" : "(", "]" : "[", "}" : "{" }

        for i in range(len(s)):
            if s[i] in matches:
                if stack and stack[-1] == matches[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        return True if not stack else False
