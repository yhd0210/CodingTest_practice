ms = input()
n = int(input())
ls = sorted([input() for i in range(n)])
max_p = max_i = 0
for i in range(n):
    L = ms.count("L") + ls[i].count("L")
    O = ms.count("O") + ls[i].count("O")
    V = ms.count("V") + ls[i].count("V")
    E = ms.count("E") + ls[i].count("E")
    p = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    if max_p < p:
        max_p = p
        max_i = i
print(ls[max_i])