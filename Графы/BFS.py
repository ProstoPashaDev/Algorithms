def bfs(v):
    q = []
    q.append(v)    
    
    while len(q) != 0:
        #print(q)
        cur = q[-1]
        q = q[:-1]
        #print(q)
        for i in range(len(a[cur])):
            if a[cur][i] == 1 and i not in ans:
                q.append(i)
                ans.append(i)



n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

ans = []
res = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    bfs(i)
    #print(ans)
    for j in ans:
        res[i][j] = 1
    ans = []
for x in res:
    print(*x)