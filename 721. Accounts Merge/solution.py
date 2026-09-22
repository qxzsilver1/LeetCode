class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UnionFind(len(accounts))

        email_to_account_idx = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account_idx:
                    uf.union(i, email_to_account_idx[email])
                else:
                    email_to_account_idx[email] = i
        
        email_group = defaultdict(list)

        for email, i in email_to_account_idx.items():
            leader = uf.find(i)
            email_group[leader].append(email)
        
        res = []

        for i, email in email_group.items():
            name = accounts[i][0]
            res.append([name] + sorted(email_group[i]))
        
        return res
