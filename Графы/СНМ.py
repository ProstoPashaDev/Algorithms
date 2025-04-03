def reset(n):
    global snm
    snm = [i for i in range(n)]
    print("RESET DONE")

def check(x, y):
    global snm
    gl = getgl(x, y)
    gl1 = gl[0]
    gl2 = gl[1]
    if gl1 == gl2:
        print("YES")
    else:
        print("NO")

def merge(x, y):    
    global snm
    gl = getgl(x, y)
    gl1 = gl[0]
    gl2 = gl[1]
    if gl1 == gl2:
        print("ALREADY " + str(x) + " " + str(y))
    else:
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

snm = []
try:
    while True:
        x = input().split()
        if x[0] == "RESET":
            reset(int(x[1]))
        elif x[0] == "JOIN":
            #print(int(x[1]), int(x[2]))
            merge(int(x[1]), int(x[2]))
        else:
            check(int(x[1]), int(x[2]))
except:
    pass