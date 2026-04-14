class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s:
            # Opening bracket
            if ch in closeToOpen.values():
                stack.append(ch)

            # Closing bracket
            elif ch in closeToOpen:
                if not stack or stack[-1] != closeToOpen[ch]:
                    return False
                stack.pop()

            else:
                return False

        return len(stack) == 0