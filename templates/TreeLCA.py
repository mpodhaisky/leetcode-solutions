class TreeLCA:
    def __init__(self, n, edges, root=1):
        self.n = n
        self.root = root
        self.LOG = (n).bit_length() + 1
        
        self.adj = [[] for _ in range(n + 1)]
        for edge in edges:
            if len(edge) == 2:
                u, v = edge
                w = 1
            else:
                u, v, w = edge
            self.adj[u].append((v, w))
            self.adj[v].append((u, w))
            
        self.depth = [0] * (n + 1)
        self.dist_to_root = [0] * (n + 1)
        self.up = [[0] * (n + 1) for _ in range(self.LOG)]
        
        self._dfs(self.root, 0, 0, 0)
        self._build_table()

    def _dfs(self, u, p, d, dist):
        self.depth[u] = d
        self.dist_to_root[u] = dist
        self.up[0][u] = p
        
        for v, w in self.adj[u]:
            if v != p:
                self._dfs(v, u, d + 1, dist + w)

    def _build_table(self):
        for i in range(1, self.LOG):
            for v in range(1, self.n + 1):
                parent = self.up[i - 1][v]
                self.up[i][v] = self.up[i - 1][parent]

    def get_lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]
        for i in range(self.LOG):
            if (diff >> i) & 1:
                u = self.up[i][u]

        if u == v:
            return u

        for i in range(self.LOG - 1, -1, -1):
            if self.up[i][u] != self.up[i][v]:
                u = self.up[i][u]
                v = self.up[i][v]

        return self.up[0][u]

    def get_distance(self, u, v):
        lca = self.get_lca(u, v)
        return self.dist_to_root[u] + self.dist_to_root[v] - 2 * self.dist_to_root[lca]
