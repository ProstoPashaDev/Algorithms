n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

dis = [10**9 for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
                a[i][j] = min(a[i][j], a[i][k] + a[k][j])
ma = -1
for x in a:
    if max(x) > ma:
        ma = max(x)
#print(a)
print(ma)