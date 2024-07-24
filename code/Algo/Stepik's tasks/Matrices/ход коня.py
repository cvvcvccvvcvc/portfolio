place = input()
d = {a: b for b,a in enumerate("abcdefgh")}
pl = [int(place[1])-1, d[place[0]]]
mat = []

for i in range(8):
    mat.append([])
    for j in range(8):
        mat[i].append(".")

for i in range(8):
    for j in range(8):
        if i == pl[0] and j == pl[1]:
            mat[i][j] = 'N'
        elif i in (pl[0]+1, pl[0]-1) and j in (pl[1]+2, pl[1]-2):
            mat[i][j] = "*"
        elif i in (pl[0]+2, pl[0]-2) and j in (pl[1]+1, pl[1]-1):
            mat[i][j] = "*"
        else:
            mat[i][j] = "."
         
for raw in mat[::-1]:
    print(*raw)