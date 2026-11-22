class Solution(object):
    def calcEquation(self, equations, values, queries):
        parent = {}
        ratio = {}  # ratio[x] = x / parent[x]

        def find(x):
            if parent[x] != x:
                root = find(parent[x])
                ratio[x] *= ratio[parent[x]]
                parent[x] = root
            return parent[x]

        def union(a, b, v):  # a / b = v
            for x in (a, b):
                if x not in parent:
                    parent[x] = x
                    ratio[x] = 1.0
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
                ratio[ra] = v * ratio[b] / ratio[a]

        for (a, b), v in zip(equations, values):
            union(a, b, v)

        ans = []
        for c, d in queries:
            if c not in parent or d not in parent or find(c) != find(d):
                ans.append(-1.0)
            else:
                ans.append(ratio[c] / ratio[d])
        return ans
