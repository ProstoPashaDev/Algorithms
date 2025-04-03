def kruscall():
    ans = 0
    for i in range(len(a)):
        if not check(a[i][0], a[i][1]):
            used[a[i][0]] = True
            used[a[i][1]] = True
            merge(a[i][0], a[i][1])
            ans += a[i][2]
    return ans

def check(x, y):
    global snm
    gl = getgl(x, y)
    gl1 = gl[0]
    gl2 = gl[1]
    if gl1 == gl2:
        return True
    else:
        return False

def merge(x, y):    
    global snm
    gl = getgl(x, y)
    gl1 = gl[0]
    gl2 = gl[1]
    snm[gl2] = gl1

def getgl(x, y):
    global snm
    gl1 = x
    gl2 = y
    while gl1 != snm[gl1]:
        snm[gl1] = snm[snm[gl1]]
        gl1 = snm[snm[gl1]]

    while gl2 != snm[gl2]:
        snm[gl2] = snm[snm[gl2]]
        gl2 = snm[snm[gl2]]
    return [gl1, gl2]

n, m = map(int, input().split())
a = []
for i in range(m):
    x, y, w = map(int, input().split())
    a.append([x, y, w])
    a.append([y, x, w])

snm = [i for i in range(n)]
used = [False for i in range(n)]
a.sort(key = lambda x: x[-1])
ans = kruscall()
if sum(used) == len(used):
    print(ans)
else:
    print("NON-CONNECTED")
