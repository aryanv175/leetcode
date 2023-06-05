class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        p, a = [], []
        vp, va= set(), set()

        # starting coords
        for r in range(m):
            p.append((r, 0))
            a.append((r, n-1))
        for c in range(n):
            p.append((0, c))
            a.append((m-1, c))
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(r, c, visited):
            visited.add((r,c))
            for di, dj in dirs:
                new_r, new_c = r + di, c + dj
                if 0 <= new_r < m and 0 <= new_c < n and matrix[r][c] <= matrix[new_r][new_c] and (new_r, new_c) not in visited:
                    dfs(new_r, new_c, visited)

        for r,c in p:
            dfs(r,c,vp)

        for r,c in a:
            dfs(r,c,va)
        
        return vp & va
