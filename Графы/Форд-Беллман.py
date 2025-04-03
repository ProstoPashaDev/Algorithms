n = int(input())
a = [[[] for j in range(n)] for i in range(n)]
for i in range(n):
    x, y, w = map(int, input().split())
    a[x-1][y-1].append(w)

dp = [30000 for j in range(n)]
dp[0] = 0
#print(a)
for k in range(1, n):
    for i in range(n):
        for j in range(n):
            for l in range(len(a[j][i])):
                if dp[j] + a[j][i][l] < dp[i]:
                    if dp[j] != 30000:
                        dp[i] = dp[j] + a[j][i][l]
print(*dp)       


