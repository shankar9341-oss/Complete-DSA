class ST:
    def __init__(self, s):
        self.n = len(s)
        self.st = [None] * (4 * self.n)
        self.build(0, self.n - 1, 1, s)

    def build(self, l, r, node, s):
        if l == r:
            self.st[node] = (1, 1, 1, s[l], s[l], 1)
            return self.st[node]

        mid = (l + r) // 2
        left = self.build(l, mid, node * 2, s)
        right = self.build(mid + 1, r, node * 2 + 1, s)
        self.st[node] = self.merge(left, right)
        return self.st[node]

    def merge(self, left, right):
        lpref, lsuf, lbest, lchar, rchar, llen = left
        rpref, rsuf, rbest, rlchar, rrchar, rlen = right

        pref = lpref
        suf = rsuf
        best = max(lbest, rbest)
        if rchar == rlchar:
            best = max(best, lsuf + rpref)
            if lpref == llen: 
                pref = llen + rpref
            if rsuf == rlen: 
                suf = rlen + lsuf

        return (pref, suf, best, lchar, rrchar, llen + rlen)

    def update(self, l, r, node, idx, val):
        if l == r:
            self.st[node] = (1, 1, 1, val, val, 1)
            return self.st[node]
            
        mid = (l + r) // 2
        if idx <= mid: 
            self.update(l, mid, node * 2, idx, val)
        else: 
            self.update(mid + 1, r, node * 2 + 1, idx, val)

        self.st[node] = self.merge(self.st[node * 2], self.st[node * 2 + 1])
        return self.st[node]

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        # q = len(queryCharacters)
        st = ST(s)
        res = []

        for i in range(len(queryCharacters)):
            st.update(0, n - 1, 1, queryIndices[i], queryCharacters[i])
            res.append(st.st[1][2])

        return res
        