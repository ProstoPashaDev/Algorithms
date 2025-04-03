def dikstra(v):
    #print(distance, visited)
    if sum(visited) == len(visited):
        return
    visited[v] = True
    for ver in range(len(a[v])):
        if a[v][ver] != -1 and visited[ver] == False:
            if distance[ver] > distance[v] + a[v][ver]:
                distance[ver] = distance[v] + a[v][ver]
                path[ver] = path[v] + [v+1]
    mi = 10**9 + 7
    versh = -1
    for i in range(n):
        if distance[i] < mi and not visited[i]:
            mi = distance[i]
            versh = i
    dikstra(versh)
    



n, s, f = map(int, input().split())
a = []
visited = [False for i in range(n)]
distance = [10**9 for i in range(n)]
distance[s-1] = 0
path = [[] for i in range(n)]
ans = [10**9 for i in range(n)]
for i in range(n):
    a.append(list(map(int, input().split())))
dikstra(s-1)
#print(path)
if s == f:
    print(s)
else:
    if len(path[f-1]) == 0:
        print(-1)
    else:
        print(*(path[f-1] + [f]))
