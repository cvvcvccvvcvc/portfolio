# put your python code here
n, m = (int(i) for i in input().split())
mat = []
for i in range(n):
    mat.append([])
    for j in range(m):
        mat[i].append(0)

co = 1       
rev = 1
for i in range(n):
    if rev == 1:
        for j in range(m):
            mat[i][j] = co
            co += 1
            rev = -1
    elif rev == -1:
        for j in range(m - 1, -1, -1):
            mat[i][j] = co
            co += 1
            rev = 1
        

for row in mat:
    for cell in row:
        print(str(cell).ljust(3),end="")
    print()