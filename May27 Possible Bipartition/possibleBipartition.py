class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        visited = [-1] * (N+1)
        color = [-1] * (N+1)
  
        graph = collections.defaultdict(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u) 

        def dfs(i,c):
            visited[i] = 1
            color[i] = c
            for v in graph[i]:
                if visited[v] == -1:
                    dfs(v,1-c)
                
        for i in graph:
            if visited[i] == -1:
                dfs(i,0)
        print(color)
        for i in graph:
            for j in graph[i]:
                if color[i] == color[j]:
                    return False
        return True
