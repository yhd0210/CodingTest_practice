n = []
for _ in range(8):
    n.append(list(map(str, list(input()))))

a = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0: #하얀칸일 경우
            if n[i][j] == 'F': #F있을 경우
                a += 1
print(a)