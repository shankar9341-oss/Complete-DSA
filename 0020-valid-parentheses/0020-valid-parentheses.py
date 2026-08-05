class Solution:
    def isValid(self, s: str) -> bool:
        mpp = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for b in s:
            if b not in mpp:
                stack.append(b)
            else:
                if not stack:
                    return False
                else:
                    pop = stack.pop()
                    if pop != mpp[b]:
                        return False
        return not stack

