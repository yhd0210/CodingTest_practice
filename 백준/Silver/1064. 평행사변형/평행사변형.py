x_1, y_1, x_2, y_2, x_3, y_3 = map(int,input().split())
re = 0.0
if x_1 == x_2 == x_3 or y_1 == y_2 == y_3 :
    re = -1.0
elif y_1-y_2 != 0 and y_1-y_3 != 0 and y_2-y_3 != 0 \
    and (x_1-x_2)/(y_1-y_2) == (x_2-x_3)/(y_2-y_3) == (x_1-x_3)/(y_1-y_3):
    re = -1.0
else :
    d1 = ((x_1-x_2)**2 + (y_1-y_2)**2) ** (1/2)
    d2 = ((x_2-x_3)**2 + (y_2-y_3)**2) ** (1/2)
    d3 = ((x_3-x_1)**2 + (y_3-y_1)**2) ** (1/2)
    re = (max(d1, d2, d3) - min(d1, d2, d3)) * 2
print(re)