def xor(str1, str2):
    return bool(str1) != bool(str2)

def dfs(v, w):
    global k
    if sum(visited) == len(visited):
        return
    visited[v] = True
    for ver in range(n):
        if not visited[ver] and a[v][ver] != -1 and xor(w, a[v][ver]) != 0:
            k += 1
            dfs(ver, xor(w, a[v][ver]))


n = int(input())
a = [[-1 for i in range(n)] for j in range(n)]
for i in range(n-1):
    x, y, w = map(int, input().split())
    a[x-1][y-1] = w

for i in range(n):
    visited = [False for i in range(n)]
    k = 1
    dfs(i, 0)
    print(sum(visited))