class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        email_idx = {} # email -> id
        emails = [] # set of emails of all accounts
        email_to_acc = {} # email_index -> account_Id

        m = 0
        
        for acc_idx, a in enumerate(accounts):
            for i in range(1, len(a)):
                email = a[i]
                if email in email_idx:
                    continue
                emails.append(email)
                email_idx[email] = m
                email_to_acc[m] = acc_idx
                m += 1

        adj = [[] for _ in range(m)]
        
        for a in accounts:
            for i in range(2, len(a)):
                id1 = email_idx[a[i]]
                id2 = email_idx[a[i - 1]]
                adj[id1].append(id2)
                adj[id2].append(id1)

        email_groups = defaultdict(list) # index of acc -> list of emails
        visited = [False] * m

        def dfs(node, accId):
            visited[node] = True
            email_groups[accId].append(emails[node])
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, accId)

        for i in range(m):
            if not visited[i]:
                dfs(i, email_to_acc[i])

        res = []
        
        for acc_idx in email_groups:
            name = accounts[acc_idx][0]
            res.append([name] + sorted(email_groups[acc_idx]))

        return res
