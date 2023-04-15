x_ls = []
y_ls = []
for _ in range(3):
    x, y = map(int, input().split())
    x_ls.append(x)
    y_ls.append(y)

for i in range(3):
    if x_ls.count(x_ls[i]) == 1:
        x_res = x_ls[i]
    if y_ls.count(y_ls[i]) == 1:
        y_res = y_ls[i]
print(x_res, y_res)