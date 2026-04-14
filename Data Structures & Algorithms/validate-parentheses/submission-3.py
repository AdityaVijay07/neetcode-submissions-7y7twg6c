class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        res=[]
        for i in s:
            if i in closeToOpen.values():
                res.append(i)
            elif i in closeToOpen:
                if not res or res[-1]!=closeToOpen[i]:
                    return False
                res.pop()
            else:
                return False
        return len(res)==0